import sys
sys.path.append('lib')  # noqa: E402

from ops.charm import CharmBase
from ops.main import main


class KeystoneCharm(CharmBase):

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.start, self.on_start)

    def make_pod_spec(self):
        """Make pod specification for Kubernetes
        Returns:
            pod_spec: Pod specification for Kubernetes
        """
        spec = {
            'containers': [{
                'name': self.framework.model.app.name,
                'imageDetails': {
                },
                'ports': [{
                    'containerPort':
                    self.framework.model.config['advertised-port'],
                    'protocol': 'TCP',
                }],
            }],
        }
        return spec


if __name__ == "__main__":
    main(KeystoneCharm)
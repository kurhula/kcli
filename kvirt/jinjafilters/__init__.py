from base64 import b64encode
import os


def basename(path):
    return os.path.basename(path)


def dirname(path):
    return os.path.dirname(path)


def none(value):
    return value if value is not None else ''


def base64(value):
    if value is None:
        return None
    return str(b64encode(value.encode('utf-8')), 'utf-8')


def _type(value):
    if value is None:
        return None
    elif isinstance(value, str):
        return 'string'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, dict):
        return 'dict'
    elif isinstance(value, list):
        return 'list'


def ocpnodes(cluster, platform, masters, workers):
    masters = ['%s-master-%d' % (cluster, num) for num in range(masters)]
    workers = ['%s-worker-%d' % (cluster, num) for num in range(workers)]
    if platform in ['kubevirt', 'openstack', 'vsphere', 'packet']:
        return ["%s-bootstrap-helper" % cluster] + ["%s-bootstrap" % cluster] + masters + workers
    else:
        return ["%s-bootstrap" % cluster] + masters + workers


def certificate(value):
    if 'BEGIN CERTIFICATE' in value:
        return value
    else:
        return "-----BEGIN CERTIFICATE-----\n%s\n-----END CERTIFICATE-----" % value


jinjafilters = {'basename': basename, 'dirname': dirname, 'ocpnodes': ocpnodes, 'none': none, 'type': _type,
                'certificate': certificate, 'base64': base64}

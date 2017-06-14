#!/usr/bin/python

from ansible.module_utils.basic import *
#import os

def main():

    module = AnsibleModule( argument_spec={} )
    response = {"Hello": "World"}

    #response = os.getuid()

    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()

##!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import pexpect, os, shutil

class janstungstenkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.13.0'
    language = 'tungsten'
    language_version = '2.1'
    language_info = {
        'name': 'tungsten',
        'mimetype': 'text',
        'file_extension': '.txt',
    }
    banner = "Tungsten/Wolfram: Computational Intelligence"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            solution = pexpect.run('tungsten "' + code + '"').decode('utf-8')
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

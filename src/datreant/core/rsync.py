"""Rsync wrapper"""

import subprocess
import os

def rsync(source, dest, compress=True, backup=False, dry=False, include=None, exclude=None, rsync_path='/usr/bin/rsync'):
    opts = ['-r'] # Recursive
    
    if compress:
        opts.append('-c')
    
    if backup:
        opts.append('-b')
    
    if dry:
        opts.append('--dry-run')
    
    if include:
        opts.extend(['--include ', include])
    
    if exclude:
        if isinstance(exclude, list):
            opts.extend(["--exclude={}".format(exc) for exc in exclude])
        elif isinstance(exclude, str):
            opts.append("--exclude={}".format(exclude))
            
    source = os.path.join(source, '') # Add trailing slash
    cmd = [rsync_path] + opts + [source, dest]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        raise Exception('Syncing error: rsync returned status code {}\nStandard error: {}\nStandard output: {}'.format(p.returncode, err, out))

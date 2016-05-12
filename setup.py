update_imported_docs(version)
if exists('setup.py'):
    run('python setup.py install')
if project.requirements_file:
    run('pip install -r %s' % project.requirements_file)
build_docs(version=version)
copy_files(artifact_dir)
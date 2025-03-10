% pyScript = 'pythonfun.py';

% pyrunfile("pythonfun.py")
% pyRun =py.sys.path;
% pyRun.insert(int32(0), pyScript);
% pyRun = py.importlib.import_module(pyScript(1:end-3));
% pyRun.main();
pyrunfile('pythonfun.py')
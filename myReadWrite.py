def WritePickle(x,fname):
    """Writes the data in x to a pickle-formatted file named fname.
    Inputs:
        x = array to save to file
        fname = string, name of pickle file to save to
    """
    import pickle, os
    f = open(fname,'w')
    pickle.dump(x,f)
    f.close()
    
def ReadPickle(fname):
    """Reads the data in pickle-formatted file fname and returns it.
    Inputs:
        fname = string, name of pickle file to read from
    
    Outputs:
        x = array stored in the pickle file
    """
    import pickle, os
    f = open(fname,'r')
    x = pickle.load(f)
    f.close()
    return x
    
def WriteNumpy(x,fname):
    """Writes the data in x to a numpy-formatted file named fname.
    Inputs:
        x = array to save to file
        fname = string, name of numpy file to save to
    """
    import os
    import numpy as np
    np.save(fname,x)
    
def ReadNumpy(fname):
    """Reads the data in numpy-formatted file fname and returns it.
    
    Inputs:
        fname = string, name of numpy file to read from
    Outputs:
        x = array stored in the numpy file
    """
    import os
    import numpy as np
    x = np.load(fname)
    return x
    
def WriteNetcdf(x,xname,xtype,xdims,xdimnames,units,history,fname):
    """Writes the data in x to a netcdf file. Up to 3D.
    
    Inputs:
        x = array to save as a variable in netcdf file
        xname = string, name to give the variable
        xtype = string, data type - 'd' for double
        xdims = integer list, dimensions of x
        xdimnames = string list, names to give dimensions
        units = string, units of x
        history = string, history of this write
        fname = string, name of netcdf file to save to
    """
    import scipy.io.netcdf as spnc
    f = spnc.netcdf_file(fname,'w')
    f.history = history
    ndims = len(xdims)
    for i in range(0,ndims):
        f.createDimension(xdimnames[i], xdims[i])
    if (ndims==1):
        a = f.createVariable(xname, xtype, (xdimnames[0]))
        a[:] = x
    elif (ndims==2):
        a = f.createVariable(xname, xtype, (xdimnames[0],xdimnames[1]))
        a[:] = x
    elif (ndims==3):
        a = f.createVariable(xname, xtype, (xdimnames[0],xdimnames[1],
                                            xdimnames[2]))
        a[:] = x
    else:
        return
    a.units = units
    f.close()
    
def ReadNetcdf(fname,varname):
    """Reads the variable varname in the netcdf file fname.
    
    Inputs:
        fname = string, name of netcdf file to read from
        varname = string, name of variable to read
    
    Outputs:
        x = array stored in the netcdf file
    """
    import numpy as np
    import scipy.io.netcdf as spnc
    f = spnc.netcdf_file(fname,'r')
    v = f.variables[varname]
    x = np.copy(v[:])
    f.close()
    return x
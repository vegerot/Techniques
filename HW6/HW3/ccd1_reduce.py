import numpy as np
from astropy.io import fits
from astropy.io.fits import getheader

files=np.genfromtxt("files.list",dtype=None,names=('filename'))
infiles=files['filename']

for i in range (0,len(infiles)):
   print i, infiles[i]
   sci_fn = infiles[i]
   out= "trim\_"+infiles[i]
   sci_hdulist = fits.open(sci_fn)
   data = sci_hdulist[0].data.astype(np.float)
   trimmed=data[:,:320]
   hdu = fits.PrimaryHDU(trimmed)
   hdu.writeto(out)


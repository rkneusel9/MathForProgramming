#
#  file:  ifs.py
#
#  Plot IFS fractals
#
#  RTK, 29-Jun-2022
#  Last update:  25-Oct-2023
#
###############################################################

import sys
import numpy as np
import matplotlib.pylab as plt


###############################################################
#  IFS
#
class IFS:
    """Iterated Function System fractals"""

    MAPS = {
        "circle": {
            "nmaps":4, 
            "probs": [0.25, 0.25, 0.25, 0.25],
            "maps": [
                [[.2929, -.2929, .5], [.2929, .2929, .5], [0,0,1]],
                [[-.2929, .2929, .5], [-.2929, -.2929, .5], [0,0,1]],
                [[.2929, .2929, .5], [-.2929, .2929, .5], [0,0,1]],
                [[-.2929,-.2929,.5], [.2929,-.2929,.5], [0,0,1]]]},
        "dragon": {
            "nmaps":2, 
            "probs": [0.5, 0.5],
            "maps": [
                [[.5, -.5, 0], [.5, .5, 0], [0,0,1]],
                [[-.5, -.5, 1], [.5,-.5,0], [0,0,1]]]},
        "fern": {
            "nmaps":4, 
            "probs":[0.75, 0.115, 0.115, 0.02],
            "maps":[
                [[.81, .07, .12], [-.04, .84, .195], [0,0,1]],  
                [[.18, -.25, .12], [.27, .23, .02], [0,0,1]],
                [[.19, .275, .16], [.238, -.14, .12], [0,0,1]],
                [[.0235, .087, .11], [.045, .1666, 0], [0,0,1]]]},
        "koch": {
            "nmaps":4, 
            "probs":[0.25,0.25,0.25,0.25],
            "maps":[[[0.333, 0, 0], [0, 0.333, 0], [0,0,1]],
                    [[0.167, -.288, .333], [.288, .167, 0], [0,0,1]],
                    [[.167, .288, .5], [-.288, .167, .288], [0,0,1]],
                    [[.333, 0, .667], [0, .333, 0], [0,0,1]]]},
        "shell": {
            "nmaps":2, 
            "probs":[0.955, 0.045],
            "maps":[
                [[.96, .15,-.08], [-.15, .96, .0861], [0,0,1]],
                [[.11, -.05, 1.11], [.05, .11, .8], [0,0,1]]]},
        "sierpinski": {
            "nmaps":3, 
            "probs":[0.3333,0.3333,0.3333],
            "maps":[
                [[.5, 0, 0], [0, .5, 0], [0,0,1]],
                [[.5, 0, .5], [0, .5, 0], [0,0,1]],
                [[.5, 0, .25], [0, .5, .5], [0,0,1]]]},
        "tree": {
            "nmaps":6, 
            "probs":[.05, .05, .4, .05, .05, .4],
            "maps":[
                [[.03, 0, -5e-3], [0, .48, 0], [0,0,1]],
                [[.035, 0, .01], [0, -.44, .21], [0,0,1]],
                [[.41, -.41, -0.1], [.41, .41, .23], [0,0,1]],
                [[.03, 0, .01], [0, .48, 0], [0,0,1]],
                [[.035,0, -7e-3], [0, .41, .02], [0,0,1]],
                [[.41, .41, .01], [-.41, .41, .23], [0,0,1]]]},
        "thistle": {
            "nmaps":4, 
            "probs":[0.75, 0.115, 0.115, 0.02],
            "maps":[
                [[-.81, .07, .12], [.04, .84, .195], [0,0,1]],  
                [[.18, -.25, .12], [.27, .23, .02], [0,0,1]],
                [[.19, .275, .16], [.238, -.14, .12], [0,0,1]],
                [[.0235, .087, .11], [.045, .1666, 0], [0,0,1]]]},
        #  the following from Paul Bourke, see http://paulbourke.net/fractals/ifs/
        #  used with permission
        "maple": {
            "nmaps": 4,
            "probs": [0.25,0.25,0.25,0.25],
            "maps": [
                [[0.14,0.01,-0.08],[0.00,0.51,-1.31],[0,0,1]],
                [[0.43,0.52,1.49],[-0.45,0.5,-0.75],[0,0,1]],
                [[0.45,-0.49,-1.62],[0.47,0.47,-0.74],[0,0,1]],
                [[0.49,0.00,0.02],[0.00,0.51,1.62],[0,0,1]]]},
        "spiral": {
            "nmaps": 3,
            "probs": [0.90,0.05,0.05],
            "maps": [
                [[0.787879,-0.424242,1.758647],[0.242424,0.859848,1.408065],[0,0,1]],
                [[-0.121212,0.257576,-6.721654],[0.151515,0.053030,1.377236],[0,0,1]],
                [[0.181818,-0.136364,6.086107],[0.090909,0.181818,1.568035],[0,0,1]]]},
        "mandel": {
            "nmaps": 2,
            "probs": [0.5,0.5],
            "maps": [
                [[0.2020,-0.8050,-0.3730],[-0.6890,-0.3420,-0.6530],[0,0,1]],
                [[0.1380,0.6650,0.6600],[-0.5020,-0.2220,-0.2770],[0,0,1]]]},
       "tree2": {
            "nmaps": 7,
            "probs": [0.142857,0.142857,0.142857,0.142857,0.142857,0.142857,0.142857],
            "maps": [
                [[0.05,0.0,-0.06],[0.0,0.4,-0.47],[0,0,1]],
                [[-0.05,0.0,-0.06],[0.0,-0.4,-0.47],[0,0,1]],
                [[0.03,-0.14,-0.16],[0.0,0.26,-0.01],[0,0,1]],
                [[-0.03,0.14,-0.16],[0.0,-0.26,-0.01],[0,0,1]],
                [[0.56,0.44,0.3],[-0.37,0.51,0.15],[0,0,1]],
                [[0.19,0.07,-0.2],[-0.1,0.15,0.28],[0,0,1]],
                [[-0.33,-0.34,-0.54],[-0.33,0.34,0.39],[0,0,1]]]},
        "tree3": {
            "nmaps": 5,
            "probs": [0.2,0.2,0.2,0.2,0.2],
            "maps": [
                [[0.1950,-0.4880,0.4431],[0.3440,0.4430,0.2452],[0,0,1]],
                [[0.4620,0.4140,0.2511],[-0.2520,0.3610,0.5692],[0,0,1]],
                [[-0.6370,0.0000,0.8562],[0.0000,0.5010,0.2512],[0,0,1]],
                [[-0.0350,0.0700,0.4884],[-0.4690,0.0220,0.5069],[0,0,1]],
                [[-0.0580,-0.0700,0.5976],[0.4530,-0.1110,0.0969],[0,0,1]]]},
        "fern2": {
            "nmaps": 4,
            "probs": [0.1, 0.08, 0.08, 0.74],
            "maps": [
                [[0,0,0],[0,0.16,0],[0,0,1]],
                [[0.2,-0.26,0],[0.23,0.22,1.6],[0,0,1]],
                [[-0.15,0.28,0],[0.26,0.24,0.44],[0,0,1]],
                [[0.75,0.04,0],[-0.04,0.85,1.6],[0,0,1]]]},
        "dragon2": {
            "nmaps": 2,
            "probs": [0.8,0.2],
            "maps": [
                [[0.824074,0.281428,-1.882290],[-0.212346,0.864198,-0.110607],[0,0,1]],
                [[0.088272,0.520988,0.785360],[-0.463889,-0.377778,8.095795],[0,0,1]]]},
    }

    def RandomMaps(self):
        """Generate a random mapping"""
        
        def mapping():
            """Find a contracting mapping"""
            while (True):
                a,b,c,d,e,f = -1 + 2*np.random.random(6)
                if (a*a+d*d) >= 1:
                    continue
                if (b*b+e*e) >= 1:
                    continue
                if a*a+b*b+d*d+e*e - (a*e-d*b)**2 >= 1:
                    continue
                break
            return [[a,b,c],[d,e,f],[0,0,1]]

        nmaps = 2 + int(4*np.random.random()) # [2,5]
        probs = np.random.random(nmaps)
        probs = probs / probs.sum()

        maps = []
        for k in range(nmaps):
            maps.append(mapping())

        return nmaps, probs, np.array(maps)


    def ChooseMap(self):
        """Select a map"""
        
        r = np.random.random()
        a = 0.0
        k = 0
        for i in range(self.nmaps):
            if (r > a):
                k = i
            else:
                return k
            a += self.probs[i]
        return k

    def GeneratePoints(self):
        """Generate the requested fractal points"""

        self.xy = np.zeros((self.npoints,3))

        #  Transient
        xy = np.array([np.random.random(), np.random.random(), 1.0])
        for i in range(100):
            m = self.maps[self.ChooseMap(),:,:]
            xy = m @ xy
        
        #  Keep these
        for i in range(self.npoints):
            k = self.ChooseMap()
            m = self.maps[k,:,:]
            xy = m @ xy
            self.xy[i,:] = [xy[0],xy[1],k]

    def StoreFractal(self, outfile, plot=True):
        """Store the fractal"""

        if (not plot):
            np.savetxt(outfile, self.xy)
            return

        #  otherwise, generate the plot and store it
        if (self.rmaps):
            print()
            print("%d maps" % self.nmaps)
            print("probs:\n    ", end="")
            print(self.probs)
            print("maps:")
            print(self.maps)
            print()

        x = self.xy[:,0]
        y = self.xy[:,1]
        m = self.xy[:,2]
        
        fig, ax = plt.subplots()

        if (self.ctype != 'maps'):
            ax.plot(x,y, marker=',', linestyle='none', color='#'+self.ctype)
        else:
            colors = np.array(['r','g','b','c','m','k','y'])
            for i in range(int(m.max())+1):
                k = np.where(m == i)[0]
                ax.plot(x[k],y[k], marker=',', linestyle='none', color=colors[i%len(colors)])
            
        ax.set_aspect('equal')
        plt.axis('off')
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.savefig(outfile, dpi=300)
        if (self.show):
            plt.show()
        else:
            plt.close()

    def GetPoints(self):
        return self.xy

    def __init__(self, npoints, name, ctype, show=False):
        self.x = 1  # always start at 1
        self.npoints = npoints
        self.name = name
        self.ctype = ctype
        self.show = show

        if (name == "random"):
            self.rmaps = True
            self.nmaps, self.probs, self.maps = self.RandomMaps()
        else:
            self.rmaps = False
            try:
                self.nmaps = self.MAPS[name]["nmaps"]
                self.probs = np.array(self.MAPS[name]["probs"])
                self.maps = np.array(self.MAPS[name]["maps"])
            except:
                raise ValueError("No such map: %s" % name)


#
#  main
#
def main():
    if (len(sys.argv) == 1):
        print()
        print("ifs <points> <output> <fractal>")
        print()
        print("  <points>   - number of points to calculate")
        print("  <output>   - output image")
        print("  <fractal>  - name from the list below or 'random'")
        print("  <color>    - <hex> (no '#')|maps")
        print()
        maps = IFS(10,"fern","green",None).MAPS
        for m in maps:
            print("%s " % m, end="")
        print()
        print()
        exit(0)

    npoints = int(sys.argv[1])
    outfile = sys.argv[2]
    name = sys.argv[3]
    ctype = sys.argv[4]

    app = IFS(npoints, name, ctype, show=True)
    app.GeneratePoints()
    app.StoreFractal(outfile)


#  Parse the command line if not imported
if (__name__ == "__main__"):
    main()


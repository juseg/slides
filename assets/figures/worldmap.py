#!/usr/bin/env python

"""Plot world map with glaciers and workplaces."""

import os.path
import zipfile
import hyoga
import matplotlib.pyplot as plt
import cartopy


def add_countries(ax, scale=None, **kwargs):
    """Add Natural Earth Data countries."""
    return ax.add_feature(
        cartopy.feature.NaturalEarthFeature(
            category='cultural', name='admin_0_countries', scale=scale),
        **kwargs)


def add_glaciers(ax, scale=None, **kwargs):
    """Add Natural Earth Data glaciers."""
    return ax.add_feature(
        cartopy.feature.NaturalEarthFeature(
            category='physical', name='glaciated_areas', scale=scale),
        **kwargs)


def add_paleoglaciers(ax, **kwargs):
    """Add Ehlers et al. (2011) paleoglaciers."""
    ### WARNING: these data fail to plot on pyshp 2.1.2 (needs 2.1.3, see issue #207)
    paths = download_paleoglaciers()
    return tuple(add_broken_shapefile(ax, path, **kwargs) for path in paths)


def add_paleoglaciers_bat19(ax, **kwargs):
    """Add Batchelor et al. (2019) paleoglaciers."""
    paths = download_paleoglaciers_bat19()
    return tuple(add_broken_shapefile(ax, path, **kwargs) for path in paths)


def add_broken_shapefile(ax, filename, **kwargs):
    """Ehlers et al. (2011) data has duplicates."""
    ax = ax or plt.gca()
    crs = cartopy.crs.PlateCarree()
    shp = cartopy.io.shapereader.Reader(filename)
    geometries = []
    for geom in shp.geometries():
        if geom not in geometries:
            geometries.append(geom)
    return ax.add_geometries(geometries, crs, **kwargs)


def download_paleoglaciers():
    """Download Ehlers et al. (2011) paleoglaciers in cache dir."""
    url = ('http://static.us.elsevierhealth.com/ehlers_digital_maps/'
           'digital_maps_02_all_other_files.zip')
    zipfilename = hyoga.demo._download(url)
    cachedir = os.path.dirname(zipfilename)
    basenames = 'lgm', 'lgm_alpen'
    for basename in basenames:
        for ext in ('dbf', 'shp', 'shx'):
            filename = basename + '.' + ext
            if not os.path.isfile(os.path.join(cachedir, filename)):
                with zipfile.ZipFile(zipfilename, 'r') as archive:
                    archive.extract(filename, path=cachedir)
    return (os.path.join(cachedir, b+'.shp') for b in basenames)


def download_paleoglaciers_bat19():
    """Download Batchelor et al. (2019) paleoglaciers in cache dir."""
    files = {'https://osf.io/gzkwc/download': 'LGM_best_estimate.dbf',
             'https://osf.io/xm6tu/download': 'LGM_best_estimate.prj',
             'https://osf.io/9bjwn/download': 'LGM_best_estimate.shx',
             'https://osf.io/9yhdv/download': 'LGM_best_estimate.shp'}
    for url, filename in files.items():
        filepath = hyoga.demo._download(url, filename=filename)
    return (filepath, )

def add_study_areas(ax, **kwargs):
    ax = ax or plt.gca()
    regions = {
        'Alps':         [150e3, 1050e3, 4820e3, 5420e3],
        'Bowdoin':      [350e3, 650e3, 8500e3, 8800e3],
        'Cordillera':   [-2500e3, -1000e3, 0e3, 3000e3]}
    projections = {
        'Alps':         cartopy.crs.UTM(32),
        'Bowdoin':      cartopy.crs.UTM(19),
        'Cordillera':   cartopy.crs.LambertConformal(central_longitude=-95,
            central_latitude=49, standard_parallels=(49, 77))}
    for name, reg in regions.items():
        w, e, s, n = reg
        x = [w, e, e, w, w]
        y = [s, s, n, n, s]
        ax.plot(x, y, color='tab:red', transform=projections[name])

    # add text labels
    lonlat = cartopy.crs.PlateCarree()
    kwargs = dict(color='tab:red', fontweight='bold', ha='center', va='center',
                  transform=lonlat)
    ax.text(-145, 50, 'Cordilleran\nice sheet', **kwargs)
    ax.text(-60, 85, 'Bowdoin\nGlacier', **kwargs)
    ax.text(10, 40, 'Alps', **kwargs)


def add_workplaces(ax, **kwargs):
    # IDEA use GeoDataFrame.to_crs() and plot midpoint arrows
    ax = ax or plt.gca()
    workplaces = {
        'Lille':     (  3.06, 50.63),
        'Paris':     (  2.35, 48.86),
        'Trondheim': ( 10.39, 63.43),
        'Grenoble':  (  5.72, 45.17),
        'Stockholm': ( 18.07, 59.33),
        'Potsdam':   ( 13.07, 52.40),
        'Zürich':    (  8.54, 47.37),
        'Sapporo':   (141.35, 43.07),
        '':          (  8.54, 47.37),
        'Anafi':     ( 25.80, 36.37),
        'Bergen':    (  5.33, 60.39),
        'Brussels':  (  4.35, 50.85)}
    lon, lat = zip(*workplaces.values())
    proj = cartopy.crs.Geodetic()
    ax.plot(lon, lat, color='0.25', marker='*', ms=8, transform=proj)
    ax.plot(
        lon[-1], lat[-1], marker='o', mec='0.25', mew=2, mfc='none', ms=12,
        transform=proj)

    # add text labels
    for name, (lon, lat) in workplaces.items():
        xtext = (8 if (lon > 10) and (lon < 90) else -8)
        ytext = (8 if name == 'Brussels' else 0)
        ax.annotate(
            name,
            xy=(lon, lat), xytext=(xtext, ytext),
            xycoords=proj._as_mpl_transform(ax), textcoords='offset points',
            ha=('left' if xtext > 0 else 'right'), va='center',
            color='0.25', fontweight='bold')


def main():
    """Main program called during execution."""

    # initialize figure
    fig = plt.figure(figsize=(9.6, 7.2))
    fig.patch.set_facecolor('none')
    proj = cartopy.crs.Orthographic(central_longitude=0, central_latitude=60)
    proj.threshold /= 100  # better line interpolation
    ax = fig.add_axes([0, 0, 1, 1], projection=proj)
    ax.patch.set_facecolor('0.9')
    ax.spines['geo'].set_edgecolor('none')

    # ax.set_extent does not work well with ortho proj
    ax.set_xlim((-6.4e6, 6.4e6))
    ax.set_ylim((-3.2e6, 6.4e6))

    # add land mask
    # FIXME hyoga.open.natural_earth().to_crs() fills are buggy on ortho proj.
    add_countries(ax=ax, alpha=0.25, facecolor='k', scale='110m')
    fig.savefig(__file__[:-3]+'_countries')

    # add glaciers
    add_glaciers(ax=ax, edgecolor='tab:blue', facecolor='tab:blue',
                 scale='50m', zorder=2)
    fig.savefig(__file__[:-3]+'_glaciers')

    # add paleoglaciers
    crs = '+proj=ortho +lon_0=0 +lat_0=60'
    hyoga.open.paleoglaciers().to_crs(crs).plot(
        ax=ax, alpha=0.5, facecolor='tab:blue', zorder=1)
    fig.savefig(__file__[:-3]+'_paleoglaciers')

    # add study areas
    add_study_areas(ax=ax)
    fig.savefig(__file__[:-3]+'_studyareas')

    # add workplaces
    add_workplaces(ax=ax)
    fig.savefig(__file__[:-3]+'_workplaces')

if __name__ == '__main__':
    main()

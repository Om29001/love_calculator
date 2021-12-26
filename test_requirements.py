import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

# dependencies can be any iterable with strings, 
# e.g. file line-by-line iterator
dependencies = [
  'Werkzeug>=0.6.1',
  'Flask>=0.9',
]

# here, if a dependency is not met, a DistributionNotFound or VersionConflict
# exception is thrown. 
pkg_resources.require(dependencies)
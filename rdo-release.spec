Name:           rdo-release
#Version:        7
# setting Version to grizzly my be a bad idea, but it makes it clear to the user
# that is is the grizzly version without having to change the package name
# Alternativly I would set it to 7 (8 = Havana etc...)
Version:        grizzly 
Release:        1
Summary:        RDO repository configuration

Group:          System Environment/Base
License:        Apache2

URL:            http://repos.fedorapeople.org/repos/openstack/
Source0:        rdo-release.repo

BuildArch:      noarch

%description
This package contains the RDO repository

%install
install -p -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/rdo-release.repo

%files
%{_sysconfdir}/yum.repos.d/rdo-release.repo

%post

# set baseurl (will this be moved to rdo url)
# baseurl=http://repos.fedorapeople.org/repos/openstack/openstack-grizzly/fedora-$releasever/
# baseurl=http://repos.fedorapeople.org/repos/openstack/openstack-grizzly/epel-6/

DIST=fedora
RELEASEVER='$releasever'
grep -i fedora /etc/redhat-release > /dev/null
if [ $? != 0 ] ; then
    DIST=epel # Should this be something else (maybe el)?
    # $releasever doesn't seem to be a reliable way to get the major version on RHEL
    # e.g. if distroverpkg isn't present in yum.conf mine was set to 6Server
    # because this was the version of the package redhat-release-server-6Server
    RELEASEVER=$(sed -e 's/.*release \([0-9]\+\).*/\1/' /etc/redhat-release)
fi

sed -i -e "s/%DIST%/$DIST/g" %{_sysconfdir}/yum.repos.d/rdo-release.repo
sed -i -e "s/%RELEASEVER%/$RELEASEVER/g" %{_sysconfdir}/yum.repos.d/rdo-release.repo

%changelog
* Wed Mar 27 2013 Derek Higgins <derekh@redhat.com> - rdo-release-grizzly-1
- Creating Package

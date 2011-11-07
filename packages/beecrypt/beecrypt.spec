Summary: BeeCrypt Cryptography Library
Name: beecrypt
Version: 4.2.1
Release: 2
Group: System Environment/Libraries
License: GPL
Distribution: LightCube OS
Vendor: LightCube Solutions
URL: http://beecrypt.sourceforge.net
Source0: http://iweb.dl.sourceforge.net/project/beecrypt/beecrypt/4.2.1/beecrypt-4.2.1.tar.gz

BuildRequires: digest(sha1:%{SOURCE0}) = b1c62c2480c79302a8ca5c09063b3d654275eae0
BuildRequires: python-devel

%description
BeeCrypt aims to provide a strong and fast cryptography toolkit.

%package devel
Summary: Headers and libraries for developing with %{name}
Group: Development/Libraries
Requires: %{name} >= %{version}

%description devel
Headers and libraries for developing with %{name}

%package python
Summary: Libraries for using %{name} with Python
Group: Development/Librares
Requires: python(abi) = 2.7

%prep
%setup -q

%build
export CFLAGS="-Os -pipe"
./configure \
  --prefix=/usr \
  --libdir=/usr/%{_lib} \
  --disable-openmp
make %{PMFLAGS}

%install
make DESTDIR=%{buildroot} install
%{strip}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
/usr/%{_lib}/libbeecrypt.so.*

%files devel
%defattr(-,root,root)
/usr/include/beecrypt
/usr/%{_lib}/libbeecrypt.a
/usr/%{_lib}/libbeecrypt.la
/usr/%{_lib}/libbeecrypt.so

%files python
/usr/lib/python2.7/site-packages/_bc.a
/usr/lib/python2.7/site-packages/_bc.la
/usr/lib/python2.7/site-packages/_bc.so

%changelog
* Mon Nov 07 2011 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 4.2.1-2
- Optimize for size

* Sun Apr 11 2010 Jeremy Huntwork <jhuntwork@lightcubesolutions.com> - 4.2.1-1
- Initial version

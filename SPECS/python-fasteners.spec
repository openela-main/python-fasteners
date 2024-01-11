%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

%if 0%{?rhel} > 7
%global with_python2 0
%else
%global with_python2 1
%endif

%global pypi_name fasteners

Name:           python-%{pypi_name}
Version:        0.14.1
Release:        14%{?dist}
Summary:        A python package that provides useful locks

License:        ASL 2.0
URL:            https://github.com/harlowja/fasteners
Source0:        https://codeload.github.com/harlowja/fasteners/tar.gz/%{version}#/%{pypi_name}-%{version}.tar.gz
Patch0:         fasteners-monotonic.patch
Patch1:         remove-testtools.patch
BuildArch:      noarch


%description
A python package that provides useful locks.


%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        A python package that provides useful locks
Obsoletes:      python-%{pypi_name} < 0.13.0-3
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-six
# tests
BuildRequires:  python2-nose
BuildRequires:  python2-monotonic
BuildRequires:  python2-futures
Requires:       python2-six
Requires:       python2-monotonic

%description -n python2-%{pypi_name}
A python package that provides useful locks.
%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        A python package that provides useful locks
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-six
BuildRequires:  python3-devel
# tests
BuildRequires:  python3-nose

Requires:       python3-six

%description -n python3-%{pypi_name}
A python package that provides useful locks.

%endif



%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
%if 0%{?with_python2}
%py2_build
%endif # with_python2

%if 0%{?with_python3}
%py3_build
%endif # with_python3

%install
%if 0%{?with_python2}
%py2_install
%endif # with_python2

%if 0%{?with_python3}
%py3_install
%endif # with_python3

%check
%if 0%{?with_python2}
nosetests-%{python2_version}
%endif # with_python2

%if 0%{?with_python3}
nosetests-%{python3_version}
%endif # with_python3

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}/
%{python2_sitelib}/%{pypi_name}-*.egg-info/
%endif # with_python2

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/
%endif # with_python3


%changelog
* Tue Jun 19 2018 Petr Viktorin <pviktori@redhat.com> - 0.14.1-14
- Drop the python-testtools build dependency

  The testtools module adds some extensions to unittest, but none of these
  extensions are actually used in python-fasteners tests (or they've been
  added back to unittest years ago, and thus aren't extensions any more).

* Tue Jun 05 2018 Troy Dawson <tdawson@redhat.com> - 0.14.1-13
- Do not do python2 in RHEL8

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.14.1-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.14.1-10
- Fix monotonic req on py3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.14.1-7
- Rebuild for Python 3.6

* Mon Aug 29 2016 Matthias Runge <mrunge@redhat.com> - 0.14.1-6
- Use time.monotonic if available (Python3 > 3.2)
  patch thanks to Ville Skyttä (rhbz#1294335)
- modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 16 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 0.14.1-4
- Spec cleanups

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Matthias Runge <mrunge@redhat.com> - 0.14.1-2
- update to 0.14.1 (rhbz#1281772)
- fix python_provide

* Mon Nov 16 2015 Matthias Runge <mrunge@redhat.com> - 0.13.0-3
- Fix build

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 28 2015 Matthias Runge <mrunge@redhat.com> - 0.13.0-1
- update to 0.13.0 (rhbz#1256153)

* Mon Jun 22 2015 Matthias Runge <mrunge@redhat.com> - 0.12.0-1
- update to 0.12.0 (rhbz#1234253)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Matthias Runge <mrunge@redhat.com> - 0.9.0-2
- switch to github sourcecode, license included
- add tests, fix conditionals for python3

* Thu Jun 11 2015 Matthias Runge <mrunge@redhat.com> - 0.9.0-1
- Initial package. (rhbz#1230548)

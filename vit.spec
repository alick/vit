%global name vit
%global branch 1.3-copr
%global version 1.3.dev
%global build_date %(TZ=America/Chicago date +"%Y%m%d")

Name:           %{name}
Version:        %{version}
Release:        %{build_date}
Summary:        A minimalist Taskwarrior full-screen terminal interface with Vim key bindings


License:        GPLv3+
URL:            https://tasktools.org/projects/vit.html

# Obtain the tarball for a certain branch via:
Source0:        %{name}-%{version}-%{release}.tar.gz

BuildArch:      noarch
BuildRequires:  task perl(Curses) perl(Time::HiRes)
Requires:       task

%description
Features:
* Vim key bindings
* uncluttered display
* no mouse
* speed


%prep
%autosetup -n %{name}-%{version}

%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc AUTHORS CHANGES LICENSE MANIFEST README VERSION
%{_bindir}/%{name}
%{_datadir}/%{name}/commands
%{_mandir}/man1/%{name}*
%{_mandir}/man5/%{name}*


%changelog
* Mon Dec 25 2017 Alick Zhao <alick AT fedoraproject DOT org> 1.3.dev-20171225
- Fix shebang line

* Sat Dec 23 2017 Alick Zhao <alick AT fedoraproject DOT org> 1.3.dev-20171223
- Update to latest HEAD and use Macports patches

* Wed Nov 08 2017 Alick Zhao <alick AT fedoraproject DOT org> 1.3.dev-20171108
- Update spec file for automatically building the 1.3 branch on Copr

* Thu Sep 01 2016 Alick Zhao <alick AT fedoraproject DOT org> 1.3-4.gitgf0f17c
- Update to latest snapshot of 1.3 branch with fixes handling of CJK characters

* Fri Aug 26 2016 Alick Zhao <alick AT fedoraproject DOT org> 1.3-3.gita7aa5f9
- Try explicitly require perl(Time::HiRes) to build for f24+

* Fri Aug 26 2016 Alick Zhao <alick AT fedoraproject DOT org> 1.3-2.gita7aa5f9
- Update to latest snapshot of 1.3 branch with multibyte related fixes

* Sun Mar 06 2016 Alick Zhao <alick AT fedoraproject DOT org> 1.3-1.git2dd8911
- Update to latest snapshot of 1.3 branch

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jul 11 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.2-1
- Update as per reviewer comments - rhbz1112072

* Tue Jun 24 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.2-1
- Update to new 1.2 stable version

* Mon Jun 23 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.2-0.1.beta1
- Initial rpmbuild

* Mon Jun 23 2014 Ankur Sinha <sanjay.ankur@gmail.com>
- 

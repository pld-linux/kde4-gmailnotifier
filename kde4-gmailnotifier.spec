%define		orgname		gmailnotifier
%define		qt_ver		4.5.1
%define		snap		141

Summary:	Gmail Notifier, a KDE 4 plasmoid
Name:		kde4-%{orgname}
Version:	%{snap}
Release:	0.1
License:	GPL v2
Group:		X11/Libraries
# svn co http://gmailnotifier.googlecode.com/svn/trunk/ gmailnotifier
Source0:	%{orgname}-r%{version}.tar.bz2
# Source0-md5:	7f9bbd0bf9f1c5d9da7fd00263afc7c0
URL:		http://gmailnotifier.googlecode.com/
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmail Notifier, a KDE 4 plasmoid.
    - Supports multiple Gmail accounts and labels
    - Shows notifications whether new e-mails arrive.
    - Supports Gmail hosted domains

%prep
%setup -q -n %{orgname}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_gmailnotifier.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_gmailnotifier.so
%dir %{_datadir}/apps/plasma-applet-gmailnotifier
%{_datadir}/apps/plasma-applet-gmailnotifier/plasma-applet-gmailnotifier.notifyrc
%{_datadir}/apps/plasma/services/gmailnotifierengine.operations
%{_datadir}/kde4/services/plasma-applet-gmailnotifier.desktop
%{_datadir}/kde4/services/plasma-dataengine-gmailnotifier.desktop

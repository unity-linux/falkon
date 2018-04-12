%define		oname		Falkon
%define		major		3
%define		libname		%mklibname %{name}private %{major}

Name:		falkon
Summary:	Cross-platform Qt Web Browser based on QtWebEngine
Version:	3.0.0
Release:	2%{?dist}
Group:		Networking/WWW
License:	GPLv3+ and BSD and LGPLv2+ and GPLv2+ and MPL
URL:		http://www.qupzilla.com/
Source0:	http://download.kde.org/stable/falkon/3.0/src/%{name}-%{version}.tar.xz
Patch0:		falkon-3.0.0-system-qtsingleapplication.patch
# reenable native scrollbars by default (upstream disabled them in 2.1.2)
Patch1:		falkon-3.0.0-native-scrollbars.patch
BuildRequires:	kf5-macros
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5WebChannel)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	qtsingleapplication-qt5-devel
BuildRequires:	qttools5
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(xcb-util)
BuildRequires:	pkgconfig(python3)

Requires:	%{name}-core	= %{version}-%{release}
Requires:	%{name}-plugins	= %{version}-%{release}

Obsoletes:	qupzilla < 2.2.5-2
Provides:	qupzilla = %{version}-%{release}

%description
Falkon is a new KDE web browser, previously known as QupZilla.
Following this release, there will only be one last final QupZilla
release.

Falkon is a new and very fast QtWebEngine browser. It aims to be a lightweight
web browser available through all major platforms. This project has been
originally started only for educational purposes. But from its start, Falkon
has grown into a feature-rich browser.

Falkon has all standard functions you expect from a web browser. It includes
bookmarks, history (both also in sidebar) and tabs. Above that, you can manage
RSS feeds with an included RSS reader, block ads with a builtin AdBlock plugin,
block Flash content with Click2Flash and edit the local CA Certificates
database with an SSL Manager.

Falkon's main aim is to be a very fast and very stable QtWebEngine browser
available to everyone. There are already a lot of QtWebEngine browsers available,
but they are either bound to the KDE environment (rekonq), are not actively
developed or very unstable and miss important features. But there is missing
a multiplatform, modern and actively developed browser. Falkon is trying
to fill this gap by providing a very stable browsing experience.

If you were previously using QupZilla, you can manually migrate
your profiles to Falkon by moving the config directory (usually
in ~/.config/qupzilla/).
There is no automatic migration.

%package core
Summary:	%{oname} web browser core package
Group:		Networking/WWW
Provides:	webclient
Requires:	%{libname} = %{version}-%{release}
Requires:	qtbase5-database-plugin-sqlite
Requires:	qtwebengine5

Obsoletes:	qupzilla-core < 2.2.5-2
Provides:	qupzilla-core = %{version}-%{release}

%description core
Falkon is a new KDE web browser, previously known as QupZilla.
Following this release, there will only be one last final QupZilla
release.

Falkon is a new and very fast QtWebEngine browser. It aims to be a lightweight
web browser available through all major platforms. This project has been
originally started only for educational purposes. But from its start, Falkon
has grown into a feature-rich browser.

Falkon has all standard functions you expect from a web browser. It includes
bookmarks, history (both also in sidebar) and tabs. Above that, you can manage
RSS feeds with an included RSS reader, block ads with a builtin AdBlock plugin,
block Flash content with Click2Flash and edit the local CA Certificates
database with an SSL Manager.

Falkon's main aim is to be a very fast and very stable QtWebEngine browser
available to everyone. There are already a lot of QtWebEngine browsers available,
but they are either bound to the KDE environment (rekonq), are not actively
developed or very unstable and miss important features. But there is missing
a multiplatform, modern and actively developed browser. Falkon is trying
to fill this gap by providing a very stable browsing experience.

If you were previously using QupZilla, you can manually migrate
your profiles to Falkon by moving the config directory (usually
in ~/.config/qupzilla/).
There is no automatic migration.

%package plugins
Summary:	Various plugins for %{oname} web browser
Group:		Networking/WWW
Requires:	%{name}-core = %{version}

Obsoletes:	qupzilla-plugins < 2.2.5-2
Provides:	qupzilla-plugins = %{version}-%{release}

%description plugins
Falkon Plugins are dynamically loaded shared libraries (*.so) that can extend
application in almost any way. This package contains the following plugins:

* Mouse Gestures
* Access Keys Navigation
* Personal Information Manager
* GreaseMonkey

%package gnome-keyring
Summary:	GNOME keyring plugin for %{oname} web browser
Group:		Networking/WWW
BuildRequires:	pkgconfig(gnome-keyring-1)
Requires:	%{name}-core = %{version}-%{release}

Obsoletes:	qupzilla-gnome-keyring < 2.2.5-2
Provides:	qupzilla-gnome-keyring = %{version}-%{release}

%description gnome-keyring
Plugin for %{oname} web browser that allows to store passwords in
GNOME Keyring.

%package kwallet
Summary:	Kwallet plugin for %{oname} web browser
Group:		Networking/WWW
BuildRequires:	cmake(KF5Wallet)
Requires:	%{name}-core = %{version}-%{release}

Obsoletes:	qupzilla-kwallet < 2.2.5-2
Provides:	qupzilla-kwallet = %{version}-%{release}

%description kwallet
Plugin for %{oname} web browser that allows to store passwords in Kwallet.

%package -n %{libname}
Summary:	%{oname} shared library
Group:		System/Libraries

Obsoletes:	%{_lib}qupzilla2 < 2.2.5-2
Obsoletes:	%{_lib}qupzilla-devel < 2.2.5-2

%description -n %{libname}
Shared library used by %{oname} web browser.

%prep
%setup -q
%autopatch -p1

dos2unix README.md

# unbundle qtsingleapplication
rm -fr src/lib/3rdparty/qtsingleapplication/*

%build
%cmake_kf5
%make_build

%install
%make_install -C build

%find_lang_kf5 falkon_qt
%find_lang_kf5 falkon_autoscroll_qt
%find_lang_kf5 falkon_flashcookiemanager_qt
%find_lang_kf5 falkon_gnomekeyringpasswords_qt
%find_lang_kf5 falkon_greasemonkey_qt
%find_lang_kf5 falkon_imagefinder_qt
%find_lang_kf5 falkon_kwalletpasswords_qt
%find_lang_kf5 falkon_mousegestures_qt
%find_lang_kf5 falkon_pim_qt
%find_lang_kf5 falkon_statusbaricons_qt
%find_lang_kf5 falkon_tabmanager_qt
%find_lang_kf5 falkon_testplugin_qt
%find_lang_kf5 falkon_verticaltabs_qt
cat *_qt.lang  > %{name}.lang

%files

%files core -f %{name}.lang
%doc CHANGELOG README.md
%license COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/appdata/org.kde.%{name}.appdata.xml
%dir %{_qt5_plugindir}/%{name}

%files plugins
%{_qt5_plugindir}/%{name}/*.so
%exclude %{_qt5_plugindir}/%{name}/GnomeKeyringPasswords.so
%exclude %{_qt5_plugindir}/%{name}/KWalletPasswords.so

%files gnome-keyring
%{_qt5_plugindir}/%{name}/GnomeKeyringPasswords.so

%files kwallet
%{_qt5_plugindir}/%{name}/KWalletPasswords.so

%files -n %{libname}
%{_libdir}/libFalkonPrivate.so.%{major}{,.*}

%changelog

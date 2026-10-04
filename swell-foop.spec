# TODO: use gtk4-update-icon-cache
Summary:	Swell Foop game for GNOME
Summary(pl.UTF-8):	Gra Swell Foop dla GNOME
Name:		swell-foop
Version:	50.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/swell-foop/50/%{name}-%{version}.tar.xz
# Source0-md5:	ecea9c3b9d11903bf2b3f1a367df00bc
URL:		https://wiki.gnome.org/Apps/Swell%20Foop
BuildRequires:	AppStream
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.74
BuildRequires:	gtk4-devel >= 4.15.3
BuildRequires:	libadwaita-devel >= 1.8
BuildRequires:	libgee-devel >= 0.14.0
BuildRequires:	librsvg-devel >= 2.46
BuildRequires:	meson >= 1.1
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-libadwaita >= 1.8
BuildRequires:	vala-libgee
BuildRequires:	vala-librsvg
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.74
Requires:	glib2 >= 1:2.74
Requires:	gtk4 >= 4.15.3
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.8
Requires:	libgee >= 0.14.0
Requires:	librsvg >= 2.46
Provides:	gnome-games-same-gnome
Provides:	gnome-games-swell-foop = 1:%{version}-%{release}
Obsoletes:	gnome-games-same-gnome < 1:2.30
Obsoletes:	gnome-games-swell-foop < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remove groups of balls to try and clear the screen.

%description -l pl.UTF-8
Gra, której celem jest oczyszczanie planszy poprzez usuwanie grup kul.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# swell-foop and swell-foop_libgnome-games-support po domains, swell-foop gnome help
%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/swell-foop
%{_datadir}/dbus-1/services/org.gnome.SwellFoop.service
%{_datadir}/glib-2.0/schemas/org.gnome.SwellFoop.gschema.xml
%{_datadir}/metainfo/org.gnome.SwellFoop.metainfo.xml
%{_desktopdir}/org.gnome.SwellFoop.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.SwellFoop.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.SwellFoop-symbolic.svg

# TODO: use gtk4-update-icon-cache
Summary:	Swell Foop game for GNOME
Summary(pl.UTF-8):	Gra Swell Foop dla GNOME
Name:		swell-foop
Version:	48.1
Release:	2
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/swell-foop/48/%{name}-%{version}.tar.xz
# Source0-md5:	440fb4a10fac697a719f94eb321a22df
URL:		https://wiki.gnome.org/Apps/Swell%20Foop
BuildRequires:	AppStream
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.74
BuildRequires:	gtk4-devel >= 4.10
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	libgee-devel >= 0.14.0
BuildRequires:	libgnome-games-support2-devel >= 2.0.0
BuildRequires:	librsvg-devel >= 2.46
BuildRequires:	meson >= 0.60
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.8
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-libadwaita
BuildRequires:	vala-libgee
BuildRequires:	vala-libgnome-games-support2 >= 2.0.0
BuildRequires:	vala-librsvg
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.74
Requires:	glib2 >= 1:2.74
Requires:	gtk4 >= 4.10
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.5
Requires:	libgee >= 0.14.0
Requires:	libgnome-games-support2 >= 2.0.0
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

%find_lang %{name} --with-gnome

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

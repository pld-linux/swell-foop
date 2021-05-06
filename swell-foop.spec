Summary:	Swell Foop game for GNOME
Summary(pl.UTF-8):	Gra Swell Foop dla GNOME
Name:		swell-foop
Version:	40.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/swell-foop/40/%{name}-%{version}.tar.xz
# Source0-md5:	80ab12af29143c8993433ef6b83f5e22
URL:		https://wiki.gnome.org/Apps/Swell%20Foop
BuildRequires:	appstream-glib
BuildRequires:	clutter-devel >= 1.14.0
BuildRequires:	clutter-gtk-devel >= 1.5.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	libgee-devel >= 0.14.0
BuildRequires:	libgnome-games-support-devel >= 1.7.1
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.36.0
Requires:	clutter >= 1.14.0
Requires:	clutter-gtk >= 1.5.0
Requires:	glib2-devel >= 1:2.36.0
Requires:	gtk+3 >= 3.24
Requires:	hicolor-icon-theme
Requires:	libgee >= 0.14.0
Requires:	libgnome-games-support >= 1.7.1
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%{_datadir}/metainfo/org.gnome.SwellFoop.appdata.xml
%{_datadir}/swell-foop
%{_desktopdir}/org.gnome.SwellFoop.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.SwellFoop.png
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.SwellFoop-symbolic.svg

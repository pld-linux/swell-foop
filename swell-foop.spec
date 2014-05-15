Summary:	Swell Foop
Summary(pl.UTF-8):	Gra Swell Foop dla GNOME
Name:		swell-foop
Version:	3.12.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/swell-foop/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	03c227f399f0162261f5e0f9d735e420
URL:		https://live.gnome.org/Swell%20Foop
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.14.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter >= 1.14.0
Requires:	clutter-gtk >= 1.4.0
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Provides:	gnome-games-same-gnome
Provides:	gnome-games-swell-foop = 1:%{version}-%{release}
Obsoletes:	gnome-games-same-gnome
Obsoletes:	gnome-games-swell-foop < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Remove groups of balls to try and clear the screen.

%description -l pl.UTF-8
Gra, której celem jest oczyszczanie planszy poprzez usuwanie grup kul.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/swell-foop
%{_datadir}/appdata/swell-foop.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.swell-foop.gschema.xml
%{_datadir}/swell-foop
%{_desktopdir}/swell-foop.desktop
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.png

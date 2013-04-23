Summary:	Swell Foop
Summary(pl.UTF-8):	Gra Swell Foop dla GNOME
Name:		swell-foop
Version:	3.8.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/swell-foop/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	3b9080ac6f09f28e5996be4a6f921c91
URL:		https://live.gnome.org/Swell%20Foop
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.91.6
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.16.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter >= 1.0.0
Requires:	clutter-gtk >= 0.91.6
Requires:	gtk+3 >= 3.4.0
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
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/swell-foop
%{_datadir}/glib-2.0/schemas/org.gnome.swell-foop.gschema.xml
%{_datadir}/swell-foop
%{_desktopdir}/swell-foop.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

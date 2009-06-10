Summary:	C library for parsing, writing and creating XML files or streams
Summary(pl.UTF-8):	Biblioteka obsługująca parsowanie, tworzenie i zapisywanie plików i strumieni XML
Name:		libnxml
Version:	0.18.3
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	http://www.autistici.org/bakunin/libnxml/%{name}-%{version}.tar.gz
# Source0-md5:	857f43970e7f0724d28f4ddc87085daf
URL:		http://www.autistici.org/bakunin/libnxml/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nXML is a C library for parsing, writing and creating XML 1.0 and 1.1
files or streams. It supports utf-8, utf-16be and utf-16le, ucs-4
(1234, 4321, 2143, 2312).

%description -l pl.UTF-8
nXML jest biblioteką języka C obsługującą parsowanie, zapisywanie i
tworzenie plików i strumieni XML 1.0 i 1.1. Wspiera utf-8, utf-16be i
utf-16le, ucs-4 (1234, 4321, 2143, 2312).

%package devel
Summary:	Header files for nXML library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki nXML
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nXML library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki nXML.

%package static
Summary:	Static nXML library
Summary(pl.UTF-8):	Statyczna biblioteka nXML
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nXML library.

%description static -l pl.UTF-8
Statyczna biblioteka nXML.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnxml.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

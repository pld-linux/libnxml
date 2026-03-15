Summary:	C library for parsing, writing and creating XML files or streams
Summary(pl.UTF-8):	Biblioteka obsługująca parsowanie, tworzenie i zapisywanie plików i strumieni XML
Name:		libnxml
Version:	0.18.5
Release:	1
License:	LGPL v2
Group:		Development/Libraries
Source0:	https://github.com/bakulf/libnxml/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	443fe423f1987efc3f56c553f3b49d35
URL:		https://github.com/bakulf/libnxml
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
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
Requires:	curl-devel

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libnxml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnxml.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnxml.so
%{_includedir}/nxml.h
%{_pkgconfigdir}/nxml.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnxml.a

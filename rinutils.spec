Summary:	C11 / gnu11 utilities C library by Shlomi Fish / Rindolf
Name:		rinutils
Version:	0.10.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/shlomif/rinutils/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3bf610aaf459be8c8b9aaaa38130e0ec
URL:		https://github.com/shlomif/rinutils/
BuildRequires:	cmake >= 3.5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of C headers containing macros and static functions that
are expected to work on Unix-like systems and MS Windows that have
been extracted from Shlomi Fish´s projects.

They include:
- sizeof-aware wrappers for malloc()/realloc()
- COUNT() and LAST() macros.
- DLLEXPORT symbols-modifiers.
- likely() and unlikely() CPU branch-prediction hints (see Stack
- Overflow question).
- long long sprintf()-formats
- min() and max()
- rinutils/portable_time.h for cross-platform time querying.
- Some string utilities as inline functions.
- typeof_wrap.h for C++-"auto"-like macros.
- GCC_UNUSED for silencing warnings.
- rinutils/rin_cmocka.h for reducing cmocka's boilerplate.

%package devel
Summary:	C11 / gnu11 utilities C library by Shlomi Fish / Rindolf
Group:		Development/Libraries

%description devel
This is a set of C headers containing macros and static functions that
are expected to work on Unix-like systems and MS Windows that have
been extracted from Shlomi Fish´s projects.

They include:
- sizeof-aware wrappers for malloc()/realloc()
- COUNT() and LAST() macros.
- DLLEXPORT symbols-modifiers.
- likely() and unlikely() CPU branch-prediction hints (see Stack
- Overflow question).
- long long sprintf()-formats
- min() and max()
- rinutils/portable_time.h for cross-platform time querying.
- Some string utilities as inline functions.
- typeof_wrap.h for C++-"auto"-like macros.
- GCC_UNUSED for silencing warnings.
- rinutils/rin_cmocka.h for reducing cmocka's boilerplate.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc NEWS.asciidoc README.asciidoc
%{_includedir}/rinutils
%{_pkgconfigdir}/librinutils.pc
%{_libdir}/cmake/Rinutils

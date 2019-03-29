Summary:	Library implementing the SSH2 protocol
Summary(pl.UTF-8):	Biblioteka implementująca protokół SSH2
Name:		libssh2
Version:	1.8.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://www.libssh2.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	616efd99af3d9ef731a26bed6cee9593
URL:		https://libssh2.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libssh2 is a C library implementing the SSH2 protocol according to
Internet Draft specifications SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06),
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

Supported Ciphers:
- aes256-ctr, aes192-ctr, aes128-ctr,
- aes256-cbc (aka rijndael-cbc@lysator.liu.se), aes192-cbc, aes128-cbc
- 3des-cbc
- blowfish-cbc
- cast128-cbc
- arcfour, arcfour128
- none

Supported Key Exchange Methods:
- diffie-hellman-group1-sha1
- diffie-hellman-group14-sha1
- diffie-hellman-group-exchange-sha1
- diffie-hellman-group-exchange-sha256

Supported Hostkey Types:
- ssh-rsa
- ssh-dss

Supported Compression Methods:
- zlib, zlib@openssh.com
- none

Supported Message Authentication Codes:
- hmac-sha2-256, hmac-sha2-512
- hmac-sha1, hmac-sha1-96
- hmac-md5, hmac-md5-96
- hmac-ripemd160 (hmac-ripemd160@openssh.com)
- none

%description -l pl.UTF-8
libssh2 to biblioteka C implementująca protokół SSH2 zgodnie ze
specyfikacjami Internet Draft SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06),
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

Obsługiwane szyfry:
- aes256-ctr, aes192-ctr, aes128-ctr,
- aes256-cbc (znany też jako rijndael-cbc@lysator.liu.se), aes192-cbc,
  aes128-cbc
- 3des-cbc
- blowfish-cbc
- cast128-cbc
- arcfour, arcfour128
- none

Obsługiwane metody wymiany kluczy:
- diffie-hellman-group1-sha1
- diffie-hellman-group14-sha1
- diffie-hellman-group-exchange-sha1
- diffie-hellman-group-exchange-sha256

Obsługiwane rodzaju kluczy hosta:
- ssh-rsa
- ssh-dss

Obsługiwane metody kompresji:
- zlib
- none

Obsługiwane kody uwierzytelniania wiadomości:
- hmac-sha2-256, hmac-sha2-512
- hmac-sha1, hmac-sha1-96
- hmac-md5, hmac-md5-96
- hmac-ripemd160 (hmac-ripemd160@openssh.com)
- none

%package devel
Summary:	Header files for libssh2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libssh2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel
Requires:	zlib-devel

%description devel
Header files for libssh2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libssh2.

%package static
Summary:	Static libssh2 library
Summary(pl.UTF-8):	Biblioteka statyczna libssh2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libssh2 library.

%description static -l pl.UTF-8
Biblioteka statyczna libssh2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-openssl=%{_prefix}
# AC_LIB_HAVE_LINKFLAGS adds unwanted -L/usr/lib to each LTLIB* - override it
%{__make} \
	LTLIBSSL="-lssl -lcrypto" \
	LTLIBZ="-lz"

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
%doc COPYING NEWS README RELEASE-NOTES docs/{AUTHORS,BINDINGS,TODO}
%attr(755,root,root) %{_libdir}/libssh2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libssh2.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libssh2.so
%{_libdir}/libssh2.la
%{_includedir}/libssh2*.h
%{_mandir}/man3/libssh2_*.3*
%{_pkgconfigdir}/libssh2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libssh2.a

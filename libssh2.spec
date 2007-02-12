Summary:	Library implementing the SSH2 protocol
Summary(pl.UTF-8):   Biblioteka implementująca protokół SSH2
Name:		libssh2
Version:	0.14
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libssh2/%{name}-%{version}.tar.gz
# Source0-md5:	7a44b7b38295d80bd8f80254ee135930
URL:		http://libssh2.sourceforge.net/
BuildRequires:	automake
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libssh2 is a C library implementing the SSH2 protocol according to
Internet Draft specifications SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06),
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

Supported Ciphers:  
- aes256-cbc (aka rijndael-cbc@lysator.liu.se)
- aes192-cbc
- aes128-cbc
- 3des-cbc
- blowfish-cbc
- cast128-cbc
- arcfour
- none

Supported Key Exchange Methods: 
- diffie-hellman-group1-sha1
- diffie-hellman-group14-sha1
- diffie-hellman-group-exchange-sha1

Supported Hostkey Types:  
- ssh-rsa
- ssh-dss

Supported Compression Methods:
- zlib
- none

Supported Message Authentication Codes:
- hmac-sha1
- hmac-sha1-96
- hmac-ripemd160
- hmac-ripemd160@openssh.com

%description -l pl.UTF-8
libssh2 to biblioteka C implementująca protokół SSH2 zgodnie ze
specyfikacjami Internet Draft SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06),
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

Obsługiwane szyfry:
- aes256-cbc (znany też jako rijndael-cbc@lysator.liu.se)
- aes192-cbc
- aes128-cbc
- 3des-cbc
- blowfish-cbc
- cast128-cbc
- arcfour
- none

Obsługiwane metody wymiany kluczy:
- diffie-hellman-group1-sha1
- diffie-hellman-group14-sha1
- diffie-hellman-group-exchange-sha1

Obsługiwane rodzaju kluczy hosta:
- ssh-rsa
- ssh-dss

Obsługiwane metody kompresji:
- zlib
- none

Obsługiwane kody uwierzytelniania wiadomości:
- hmac-sha1
- hmac-sha1-96
- hmac-ripemd160
- hmac-ripemd160@openssh.com

%package devel
Summary:	Header files for libssh2 library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libssh2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libssh2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libssh2.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure \
	--with-openssl=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

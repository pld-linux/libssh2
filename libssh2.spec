Summary:	Library implementing the SSH2 protocol.
Summary(pl):	Biblioteka implementuj±ca protokó³ SSH2.
Name:		libssh2
Version:	0.4
Release:	0.0.1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libssh2/%{name}-%{version}.tar.gz
# Source0-md5:	bc7125a008d2d32f233193715395c250
Patch0:		%{name}-DESTDIR.patch
URL:		http://libssh2.sourceforge.net/
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libssh2 is a C library implementing the SSH2 protocol according to
Internet Draft specifications SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

Supported Ciphers:  
- aes256-cbc (aka rijndael-cbc@lysator.liu.se)
- aes192-cbc
- aes128-cbc
- 3des-cbc
- blowfish-cbc
- cast128-cbc
- arcfour
- none**

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

#%description -l pl

%package devel
Summary:	Header files for libssh2 library
Summary(pl):	Pliki nag³ówkowe biblioteki libssh2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libssh2 library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libssh2.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-openssl=%{_prefix}
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
%doc TODO README
%attr(755,root,root) %{_libdir}/lib*.so

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

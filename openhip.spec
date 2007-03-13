Summary:	OpenHIP Host Identity Protocol usermode for Linux
Summary(pl.UTF-8):	Implementacja OpenHIP protokołu HIP
Name:		openhip
Version:	0.4
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/openhip/hip-%{version}.tgz
# Source0-md5:	68507996790ef185e8be8ecd262143d9
Source1:	http://dl.sourceforge.net/openhip/hipd-0.3.4.tgz
# Source1-md5:	4ea6d4747a8c2df2a737fd578b37fb7c
URL:		http://www.openhip.org/
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libxml2-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenHIP is a free, open-source implementation of the Host Identity
Protocol (HIP). HIP is being developed within the Internet Engineering
Task Force (IETF) and the Internet Research Task Force (IRTF) to study
and experiment with HIP and related protocols.

HIP is a specific proposal to decouple network identity from network
location in the Internet protocol stack. Historically, IP addresses
have served both functions. This dual use of IP addresses is becoming
problematic, and there have been many research efforts aimed at
studying the decoupling of identifier and locator in the network stack.
HIP is a specific proposal that uses public/private key pairs as the
host identifiers.


%description -l pl.UTF-8
OpenHIP jest otwartą implementacją protokołu HIP, rozwijanego w ramach
IETF oraz IRTF.
HIP jest propozycją rozdzielenia w stosie protokołów sieciowych
identyfikacji węzła od jego lokalizacji. Historycznie adres IP pełnił
obie te funkcje, co staje się obecnie problematyczne. HIP do
identyfikacji węzła używa pary kluczy prywatnego oraz publicznego.

%prep
%setup -q -n hip-%{version} -a1
%patch0 -p0

%build
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

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%doc AUTHORS ChangeLog NEWS README hipd-0.3.4/doc/*
%config %{_sysconfdir}/hip

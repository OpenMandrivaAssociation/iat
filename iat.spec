%define name    iat
%define version 0.1.7
%define release 3

Name: %{name}
Version: %{version}
Release: %{release}

Summary: Iso9660 Analyzer Tool
License: GPLv2+
Group: File tools
Url: https://iat.berlios.de/
Source: iat-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
iat (Iso9660 Analyzer Tool) is a tool for detecting the structure of many
types of CD-ROM image file formats, such as BIN, MDF, PDI, CDI, NRG, and B5I,
and converting them into ISO-9660.

%prep
%setup

%build
%configure
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}/%{_mandir}/man1/%{name}

cp src/%{name} %{buildroot}%{_bindir}
cp ChangeLog AUTHORS COPYING INSTALL NEWS README %{buildroot}%{_docdir}/%{name}
install -c -m 644 man/iat.1 %{buildroot}/%{_mandir}/man1/%{name}

%files
%_bindir/%{name}
%doc %{_mandir}/man1/%{name}
%{_docdir}/%{name}


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.7-2mdv2011.0
+ Revision: 619508
- the mass rebuild of 2010.0 packages

* Tue Oct 13 2009 Anne Nicolas <ennael@mandriva.org> 0.1.7-1mdv2010.0
+ Revision: 457199
- import iat


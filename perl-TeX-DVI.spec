%include	/usr/lib/rpm/macros.perl
%define	pdir	TeX
%define	pnam	DVI
Summary:	TeX::DVI perl module
Summary(pl):	Modu³ perla TeX::DVI
Name:		perl-TeX-DVI
Version:	0.101
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Font-TFM
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-TeX-DVI-Parse
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeX::DVI - writes out, parses and prints the content of DVI files.

%description -l pl
TeX::DVI - modu³ do operowania na plikach DVI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/TeX/DVI.pm
%{perl_vendorlib}/TeX/DVI
%{_mandir}/man3/*

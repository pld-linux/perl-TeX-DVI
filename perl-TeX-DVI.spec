%include	/usr/lib/rpm/macros.perl
Summary:	TeX-DVI perl module
Summary(pl):	Modu³ perla TeX-DVI
Name:		perl-TeX-DVI
Version:	0.101
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/TeX/TeX-DVI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Font-TFM
Obsoletes:	perl-TeX-DVI-Parse
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TeX-DVI - writes out, parses and prints the content of DVI files.

%description -l pl
TeX-DVI - modu³ do operowania na plikach DVI.

%prep
%setup -q -n TeX-DVI-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/TeX/DVI.pm
%{perl_sitelib}/TeX/DVI/Parse.pm
%{_mandir}/man3/*

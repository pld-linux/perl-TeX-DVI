%include	/usr/lib/rpm/macros.perl
Summary:	TeX-DVI perl module
Summary(pl):	Modu³ perla TeX-DVI
Name:		perl-TeX-DVI
Version:	0.100
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/TeX/TeX-DVI-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Font-TFM
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/TeX/DVI
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/TeX/DVI.pm
%{perl_sitelib}/TeX/DVI/Parse.pm
%{perl_sitearch}/auto/TeX/DVI

%{_mandir}/man3/*

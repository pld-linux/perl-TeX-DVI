#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	TeX
%define	pnam	DVI
Summary:	TeX::DVI perl module
Summary(pl):	Modu³ perla TeX::DVI
Name:		perl-TeX-DVI
Version:	0.101
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7f093518b1491785bf32483de312f7fe
BuildRequires:	perl-devel >= 1:5.8.0
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/TeX/DVI.pm
%{perl_vendorlib}/TeX/DVI
%{_mandir}/man3/*

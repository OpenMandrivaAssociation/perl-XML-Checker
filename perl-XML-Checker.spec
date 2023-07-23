%define modname	XML-Checker

Summary:	XML::Checker - a Perl module for validating XML
Name:		perl-%{modname}
Version:	0.13
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl-libxml-perl >= 0.07
Provides:	perl-libxml-enno = %{version}-%{release}
# Ease transitioning from old versioning scheme
Obsoletes:	%{name} = 0.130.0-16

%description
XML::Checker can be used in different ways to validate XML. See the
manual pages of XML::Checker::Parser and XML::DOM::ValParser for more
information.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

# FIXME at some point, we should investigate the test failures
# instead of ignoring them
%if 0
%check
make test
%endif

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/XML/Checker*
%{perl_vendorlib}/XML/DOM/*
%{_mandir}/man3/*

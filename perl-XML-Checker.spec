%define real_name XML-Checker

Summary:	XML::Checker - a Perl module for validating XML
Name:		perl-%{real_name}
Version:	0.13
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl-libxml-perl >= 0.07
BuildArch:	noarch
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno

%description
XML::Checker can be used in different ways to validate XML. See the
manual pages of XML::Checker::Parser and XML::DOM::ValParser for more
information.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/XML/Checker*
%{perl_vendorlib}/XML/DOM/*
%{_mandir}/man3/*



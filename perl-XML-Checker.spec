%define upstream_name    XML-Checker
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	XML::Checker - a Perl module for validating XML
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser >= 2.30
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl-libxml-perl >= 0.07
BuildArch:	noarch
Provides:	perl-libxml-enno = %{version}-%{release}

%description
XML::Checker can be used in different ways to validate XML. See the
manual pages of XML::Checker::Parser and XML::DOM::ValParser for more
information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/XML/Checker*
%{perl_vendorlib}/XML/DOM/*
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-4mdv2012.0
+ Revision: 765824
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.130.0-2
+ Revision: 667413
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 401869
- rebuild using %%perl_convert_version

* Wed Sep 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.13-6mdv2009.0
+ Revision: 287785
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.13-4mdv2008.1
+ Revision: 180642
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.13-3mdv2007.0
+ Revision: 85634
- Import perl-XML-Checker

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.13-3
- use the %%mkrel macro

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13-2mdk
- fix deps

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13-1mdk
- initial Mandriva package


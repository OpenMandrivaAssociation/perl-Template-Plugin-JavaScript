%define upstream_name	 Template-Plugin-JavaScript
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	TT filter to encode text to be safe in JavaScript
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Template::Plugin::JavaScript is a TT filter that filters text so it
can be safely used in JavaScript quotes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Template
%{_mandir}/man3/*

%changelog
* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 622949
- new version

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 410097
- rebuild using %%perl_convert_version

* Thu Mar 06 2008 Anssi Hannula <anssi@mandriva.org> 0.01-1mdv2008.1
+ Revision: 181029
- initial Mandriva release


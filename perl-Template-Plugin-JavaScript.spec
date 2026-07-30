%define upstream_name	 Template-Plugin-JavaScript
%define upstream_version 0.02
Name:		perl-%{upstream_name}
Version:	0.02
Release:	2

Summary:	TT filter to encode text to be safe in JavaScript
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Template-Plugin-JavaScript
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Template-Plugin-JavaScript-0.02.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Template::Plugin::JavaScript is a TT filter that filters text so it
can be safely used in JavaScript quotes.

%prep
%setup -q -n Template-Plugin-JavaScript-0.02

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Template
%{_mandir}/man3/*


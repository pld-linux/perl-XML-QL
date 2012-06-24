%include	/usr/lib/rpm/macros.perl
Summary:	XML-QL perl module
Summary(pl):	Modu� perla XML-QL
Name:		perl-XML-QL
Version:	0.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/XML-QL-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML-QL - An XML query language. 

%description -l pl
XML-QL - j�zyk zapyta� XML.

%prep
%setup -q -n XML-QL-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/XML/QL
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

%{perl_sitelib}/XML/QL.pm
%{perl_sitearch}/auto/XML/QL

%{_mandir}/man3/*

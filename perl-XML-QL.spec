%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	QL
Summary:	XML::QL perl module
Summary(pl):	Modu� perla XML::QL
Name:		perl-XML-QL
Version:	0.07
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2fd58d1a2ec1c36bd22d86a2a4416637
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::QL - An XML query language.

%description -l pl
XML::QL - j�zyk zapyta� XML.

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
%{perl_vendorlib}/XML/QL.pm
%{_mandir}/man3/*

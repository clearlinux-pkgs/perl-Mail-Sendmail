#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mail-Sendmail
Version  : 0.80
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Mail-Sendmail-0.80.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Mail-Sendmail-0.80.tar.gz
Summary  : 'Simple platform independent mailer'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Mail-Sendmail-license = %{version}-%{release}
Requires: perl-Mail-Sendmail-perl = %{version}-%{release}
Requires: perl(MIME::QuotedPrint)
BuildRequires : buildreq-cpan

%description
Perl 5 module Mail::Sendmail
Mail::Sendmail is a pure perl module that provides a simple
platform-independent mailer.

%package dev
Summary: dev components for the perl-Mail-Sendmail package.
Group: Development
Provides: perl-Mail-Sendmail-devel = %{version}-%{release}
Requires: perl-Mail-Sendmail = %{version}-%{release}

%description dev
dev components for the perl-Mail-Sendmail package.


%package license
Summary: license components for the perl-Mail-Sendmail package.
Group: Default

%description license
license components for the perl-Mail-Sendmail package.


%package perl
Summary: perl components for the perl-Mail-Sendmail package.
Group: Default
Requires: perl-Mail-Sendmail = %{version}-%{release}

%description perl
perl components for the perl-Mail-Sendmail package.


%prep
%setup -q -n Mail-Sendmail-0.80
cd %{_builddir}/Mail-Sendmail-0.80

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mail-Sendmail
cp %{_builddir}/Mail-Sendmail-0.80/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mail-Sendmail/b4d6080441b7932448f622518469e8da4ea1860e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mail::Sendmail.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mail-Sendmail/b4d6080441b7932448f622518469e8da4ea1860e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

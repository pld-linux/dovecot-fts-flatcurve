Summary:	FTS plugin for dovecot using Xapian
Summary(pl.UTF-8):	Wtyczka FTS dla dovecota używająca Xapian
Name:		dovecot-fts-flatcurve
Version:	0.3.3
Release:	1
License:	LGPL
Group:		Daemons
Source0:	https://github.com/slusarz/dovecot-fts-flatcurve/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	3bd17e35568cfd7fa48f2a4e1e1948d0
URL:		https://github.com/slusarz/dovecot-fts-flatcurve
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dovecot-devel
BuildRequires:	libtool
BuildRequires:	xapian-core-devel
%requires_eq_to	dovecot dovecot-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Dovecot FTS plugin to enable message indexing using the
Xapian Open Source Search Engine Library.

The plugin relies on Dovecot to do the necessary stemming. It is
intended to act as a simple interface to the Xapian storage/search
query functionality.

This driver supports match scoring and substring matches, which means
it is RFC 3501 (IMAP4rev1) compliant (although substring searches are
off by default). This driver does not support fuzzy searches, as there
is no built-in support in Xapian for it.


%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-dovecot=%{_libdir}/dovecot

%{__make} \
	dovecot_incdir=%{_includedir}/dovecot \
	moduledir=%{_libdir}/dovecot/plugins

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	moduledir=%{_libdir}/dovecot/plugins

rm -f $RPM_BUILD_ROOT%{_libdir}/dovecot/plugins/lda/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/dovecot/plugins/doveadm/lib21_doveadm_fts_flatcurve_plugin.so
%attr(755,root,root) %{_libdir}/dovecot/plugins/lib21_fts_flatcurve_plugin.so

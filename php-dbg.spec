#
# INFO: How to get working: patching, installation, using with PHPeclipse (*very* helpful):
#	http://www.phpeclipse.de/tiki-view_forum_thread.php?forumId=3&comments_parentId=3265
#
# TODO:
#	- install dbg.ini (Source1) in /etc/php/conf.d/, restart apache2
#	- do sth with php4
#	- cleaning
Summary:	dbg - PHP debbuger - extension for PHP
Name:		php-dbg
Version:	2.11.32
Release:	0.1
License:	The DBG License Version 3.0
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/dbg2/dbg-%{version}-src.tar.gz
# Source0-md5:	1ac7372bfcb4c5e13cad1248e071d70c
Source1:	dbg.ini
Patch0:		dbg-php-5.2.patch
URL:		http://dd.cron.ru/dbg/
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	dbg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBG is a a full-featured php debugger, an interactive tool that helps
you debugging php scripts. It works on a production and/or development
WEB server and allows you debug your scripts locally or remotely, from
an IDE or console. This package contain dbg extension for PHP.

%prep
%setup -q -n dbg-%{version}
%patch0 -p1

%build
phpize
%configure \
	--with-dbg-profiler \
	--enable-dbg=shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# don't remove COPYING and INSTALL
%doc AUTHORS COPYING INSTALL
%attr(755,root,root) %{php_extensiondir}/dbg.so

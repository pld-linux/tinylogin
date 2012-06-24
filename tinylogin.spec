Summary:	A tiny utility suite for login and password handling
Summary(pl):	Ma�e narz�dzie do obs�ugi logowania i hase�
Name:		tinylogin
Version:	1.02
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://tinylogin.busybox.net/downloads/%{name}-%{version}.tar.bz2
URL:		http://tinylogin.busybox.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%Description
TinyLogin is a suite of tiny utilities in a multi-call binary, which
enables your system to handle user authentication, and setting of
passwords. It is a drop-in to works nicely with BusyBox (another
multi-call binary), and makes an excellent addition to any small or
embedded system.

%description -l pl
TinyLogin to zestaw ma�ych narz�dzi w pojedynczej binarce wywo�ywanej
pod r�nymi nazwami. Narz�dzia te pozwalaj� na uwierzytelnianie
u�ytkownik�w i ustawianie hase�. TinyLogin dzia�a �adnie z BusyBoksem
(inn� binark� wywo�ywan� pod r�nymi nazwami) i stanowi doskona�y
dodatek do ka�dego ma�ego lub wbudowanego systemu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTIMIZATION="%{rpmcflags}" \
	STRIPTOOL="echo"

gzip -9nf Changelog LICENSE README TODO

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install tinylogin $RPM_BUILD_ROOT%{_bindir}
install docs/TinyLogin.1 $RPM_BUILD_ROOT%{_mandir}/man1/tinylogin.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tinylogin.links docs/tinylogin.busybox.net/*
%attr(4755,root,root) %{_bindir}/tinylogin
%{_mandir}/man1/tinylogin.1*

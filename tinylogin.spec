Summary:	A tiny utility suite for login and password handling
Summary(pl):	Ma³e narzêdzie do obs³ugi logowania i hase³
Name:		tinylogin
Version:	1.4
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/System
Source0:	http://tinylogin.busybox.net/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	44da0ff2b727455669890b24305e351d
URL:		http://tinylogin.busybox.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TinyLogin is a suite of tiny utilities in a multi-call binary, which
enables your system to handle user authentication, and setting of
passwords. It is a drop-in to works nicely with BusyBox (another
multi-call binary), and makes an excellent addition to any small or
embedded system.

%description -l pl
TinyLogin to zestaw ma³ych narzêdzi w pojedynczej binarce wywo³ywanej
pod ró¿nymi nazwami. Narzêdzia te pozwalaj± na uwierzytelnianie
u¿ytkowników i ustawianie hase³. TinyLogin dzia³a ³adnie z BusyBoksem
(inn± binark± wywo³ywan± pod ró¿nymi nazwami) i stanowi doskona³y
dodatek do ka¿dego ma³ego lub wbudowanego systemu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	OPTIMIZATION="%{rpmcflags}" \
	STRIPTOOL="echo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install tinylogin $RPM_BUILD_ROOT%{_bindir}
install docs/TinyLogin.1 $RPM_BUILD_ROOT%{_mandir}/man1/tinylogin.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc tinylogin.links docs/tinylogin.busybox.net/* Changelog LICENSE README TODO
%attr(4755,root,root) %{_bindir}/tinylogin
%{_mandir}/man1/tinylogin.1*

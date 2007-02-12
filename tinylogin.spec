Summary:	A tiny utility suite for login and password handling
Summary(pl.UTF-8):   Małe narzędzie do obsługi logowania i haseł
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

%description -l pl.UTF-8
TinyLogin to zestaw małych narzędzi w pojedynczej binarce wywoływanej
pod różnymi nazwami. Narzędzia te pozwalają na uwierzytelnianie
użytkowników i ustawianie haseł. TinyLogin działa ładnie z BusyBoksem
(inną binarką wywoływaną pod różnymi nazwami) i stanowi doskonały
dodatek do każdego małego lub wbudowanego systemu.

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

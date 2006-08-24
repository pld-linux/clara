Summary:	Cooperative Lightweight chAracter Recognizer (OCR)
Summary(pl):	Niewielkie narzêdzie do kooperatywnego rozpoznawania znaków (OCR)
Name:		clara
Version:	0.9.9
%define	snap	20031214
Release:	1.%{snap}.3
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
#Source0Download: http://www.claraocr.org/download.html
Source0:	http://www.claraocr.org/sources/%{name}-%{snap}.tar.gz
# Source0-md5:	3cd4eb76355d874f57058b19132e91d6
URL:		http://www.claraocr.org/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clara is an OCR program. OCR stands for "Optical Character
Recognition". An OCR program tries to recognize the characters from
the digital image of a paper document. The name Clara stands for
"Cooperative Lightweight chAracter Recognizer".

%description -l pl
Clara jest programem do OCR, czyli optycznego rozpoznawania znaków z
cyfrowego obrazu dokumentu.

%prep
%setup -q -n %{name}-%{snap}

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} \$(INCLUDE) \$(COPTS)" \
	LDFLAGS="%{rpmldflags}" \
	LIBPATH="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DOCDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGELOG doc/FAQ doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

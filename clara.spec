Summary:	Cooperative Lightweight chAracter Recognizer (OCR)
Summary(pl):	Niewielkie narzêdzie do kooperatywnego rozpoznawania znaków (OCR)
Name:		clara
Version:	20020402
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://mandrake.redbox.cz/Mandrake-devel/projects/claraocr/%{name}-%{version}.tar.gz
URL:		http://www.claraocr.org/
BuildRequires:	XFree86-devel
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Clara is an OCR program. OCR stands for "Optical Character
Recognition". An OCR program tries to recognize the characters from
the digital image of a paper document. The name Clara stands for
"Cooperative Lightweight chAracter Recognizer".

%description -l pl
Clara jest programem do OCR, czyli optycznego rozpoznawania znaków z
cyfrowego obrazu dokumentu.

%prep
%setup -q

%build
%{__make} all \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} \$(INCLUDE) \$(COPTS)" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DOCDIR=$RPM_BUILD_ROOT

gzip -9nf ANNOUNCE CHANGELOG doc/FAQ

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

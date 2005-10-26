Summary:	HTML to text converter
Summary(pl):	Konwerter z HTML do tekstu
Name:		vilistextum
Version:	2.6.7
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/vilistextum/%{name}-%{version}.tar.bz2
# Source0-md5:	e35ae3d99d1f90dd78a2a87adf1db8cf
URL:		http://bhaak.dyndns.org/vilistextum/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vilistextum is a small and fast HTML to text / ascii converter
specifically programmed to get the best out of incorrect html. It is
quite fault-tolerant and deals well with badly-formed or otherwise
quirky HTML. It is able to optimize for ebook reading, collapse
multiple blank lines, and create footnotes out of links.

%description -l pl
Vilistextum jest ma³ym i szybkim narzêdziem do konwersji HTML do
tekstu, zaprogramowanym do uzyskania najlepszej jako¶ci przy b³êdnym
htmlu. Jest odporny na b³êdy oraz radzi sobie z ¼le formatowanym
HTML-em. Jest tak¿e zoptymalizowany do czytania ebooków, ³±czenia
wielu pustych lini i tworzenia stopek z linkami.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*

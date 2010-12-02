%define version 0.10.26
%define release %mkrel 1
%define         _glib2          2.2
%define major 0.10
%define majorminor 0.10
%define bname gstreamer0.10
%define name %bname-plugins-good
%define gst_required_version 0.10.31

Summary: 	GStreamer Streaming-media framework plug-ins
Name: 		%name
Version: 	%version
Release: 	%release
License: 	LGPLv2+
Group: 		Sound
Source: 	http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.bz2
# (cg) Comment out for now... it seems to unstable.
#Patch2:		0002-pulsesink-share-the-PA-context-between-all-clients-w.patch
URL:            http://gstreamer.freedesktop.org/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root 
#gw for the pixbuf plugin
BuildRequires:  gtk+2-devel
BuildRequires:  glib2-devel >= %_glib2 
BuildRequires: libpng-devel >= 1.2.4-4mdk
BuildRequires: libjpeg-devel
BuildRequires: liborc-devel >= 0.4.5
BuildRequires: libvorbis-devel >= 1.0-4mdk
BuildRequires: libtheora-devel
BuildRequires: libshout-devel
BuildRequires: libv4l-devel
BuildRequires: libbzip2-devel
BuildRequires: gettext-devel
BuildRequires: taglib-devel
BuildRequires: hal-devel >= 0.5.6
BuildRequires: libgudev-devel
# libtool dep:
BuildRequires: dbus-glib-devel
%ifarch %ix86
BuildRequires: nasm => 0.90
%endif
%ifnarch %mips %arm
BuildRequires: valgrind
%endif
BuildRequires: libcheck-devel
BuildRequires: libgstreamer-plugins-base-devel >= %{gst_required_version}
BuildRequires: gstreamer0.10-plugins-base
BuildRequires: libmesaglu-devel
BuildRequires: libGConf2-devel
#gw else the tests fail: 
#https://bugzilla.gnome.org/show_bug.cgi?id=619717
BuildConflicts: %name < 0.10.23 
BuildConflicts: %bname-plugins-bad < 0.10.19
Provides:	%bname-audiosrc
Provides:	%bname-audiosink
# some plugins moved from bad to good with release 0.10.23
Conflicts: gstreamer0.10-plugins-bad < 0.10.19
# gw this is the default http source:
Suggests: %bname-soup

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that are considered to have
good quality code, correct functionality, the preferred license (LGPL
for the plug-in code, LGPL or LGPL-compatible for the supporting
library). People writing elements should base their code on these
elements.


%prep
%setup -q -n gst-plugins-good-%{version}
%apply_patches

%build
%configure2_5x  \
  --with-package-name='Mandriva %name package' \
  --with-package-origin='http://www.mandriva.com/' \
  --disable-dependency-tracking   --enable-experimental
%make

# FIXME: Some tests on mips are currently failing with timeouts
# so disable them.
%ifnarch %mips
%check
cd tests/check
make check
%endif

%install
rm -rf %buildroot gst-plugins-base-%majorminor.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std GETTEXT_PACKAGE=gst-plugins-good-%majorminor
%find_lang gst-plugins-good-%majorminor
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{majorminor}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

#blino remove development doc since we don't ship devel files
rm -rf $RPM_BUILD_ROOT%{_docdir}/docs/plugins/html

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas gstreamer-0.10

%post
%post_install_gconf_schemas %{schemas}

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f gst-plugins-good-%majorminor.lang
%defattr(-, root, root)
%doc AUTHORS COPYING README NEWS
%_sysconfdir/gconf/schemas/gstreamer-%majorminor.schemas
%_libdir/gstreamer-%majorminor/libgstalaw.so
%_libdir/gstreamer-%majorminor/libgstannodex.so
%_libdir/gstreamer-%majorminor/libgstalpha.so
%_libdir/gstreamer-%majorminor/libgstalphacolor.so
%_libdir/gstreamer-%majorminor/libgstapetag.so
%_libdir/gstreamer-%majorminor/libgstaudiofx.so
%_libdir/gstreamer-%majorminor/libgstauparse.so
%_libdir/gstreamer-%majorminor/libgstautodetect.so
%_libdir/gstreamer-%majorminor/libgstavi.so
%_libdir/gstreamer-%majorminor/libgstcairo.so
%_libdir/gstreamer-%majorminor/libgstcutter.so
%_libdir/gstreamer-%majorminor/libgstdebug.so
%_libdir/gstreamer-%majorminor/libgstdeinterlace.so
%_libdir/gstreamer-%majorminor/libgstefence.so
%_libdir/gstreamer-%majorminor/libgsteffectv.so
%_libdir/gstreamer-%majorminor/libgstflv.so
%_libdir/gstreamer-%majorminor/libgstequalizer.so
%_libdir/gstreamer-%majorminor/libgstflxdec.so
%_libdir/gstreamer-%majorminor/libgstgconfelements.so
%_libdir/gstreamer-%majorminor/libgstgdkpixbuf.so
%_libdir/gstreamer-%majorminor/libgstgoom.so
%_libdir/gstreamer-%majorminor/libgstgoom2k1.so
%_libdir/gstreamer-%majorminor/libgsthalelements.so
%_libdir/gstreamer-%majorminor/libgsticydemux.so
%_libdir/gstreamer-%majorminor/libgstid3demux.so
%_libdir/gstreamer-%majorminor/libgstimagefreeze.so
%_libdir/gstreamer-%majorminor/libgstinterleave.so
%_libdir/gstreamer-%majorminor/libgstjpeg.so
%_libdir/gstreamer-%majorminor/libgstlevel.so
%_libdir/gstreamer-%majorminor/libgstmatroska.so
%_libdir/gstreamer-%majorminor/libgstmonoscope.so
%_libdir/gstreamer-%majorminor/libgstmulaw.so
%_libdir/gstreamer-%majorminor/libgstmultifile.so
%_libdir/gstreamer-%majorminor/libgstmultipart.so
%_libdir/gstreamer-%majorminor/libgstnavigationtest.so
%_libdir/gstreamer-%majorminor/libgstossaudio.so
%_libdir/gstreamer-%majorminor/libgstoss4audio.so
%_libdir/gstreamer-%majorminor/libgstpng.so
%_libdir/gstreamer-%majorminor/libgstqtdemux.so
%_libdir/gstreamer-%majorminor/libgstreplaygain.so
%_libdir/gstreamer-%majorminor/libgstrtp.so
%_libdir/gstreamer-%majorminor/libgstrtpmanager.so
%_libdir/gstreamer-%majorminor/libgstrtsp.so
%_libdir/gstreamer-%majorminor/libgstshapewipe.so
%_libdir/gstreamer-%majorminor/libgstshout2.so
%_libdir/gstreamer-%majorminor/libgstsmpte.so
%_libdir/gstreamer-%majorminor/libgstspectrum.so
%_libdir/gstreamer-%majorminor/libgsttaglib.so
%_libdir/gstreamer-%majorminor/libgstudp.so
%_libdir/gstreamer-%majorminor/libgstvideo4linux2.so
%_libdir/gstreamer-%majorminor/libgstvideobox.so
%_libdir/gstreamer-%majorminor/libgstvideocrop.so
%_libdir/gstreamer-%majorminor/libgstvideofilter.so
%_libdir/gstreamer-%majorminor/libgstvideomixer.so
%_libdir/gstreamer-%majorminor/libgstwavenc.so
%_libdir/gstreamer-%majorminor/libgstwavparse.so
%_libdir/gstreamer-%majorminor/libgstximagesrc.so
%_libdir/gstreamer-%majorminor/libgsty4menc.so
%dir %_datadir/gstreamer-%majorminor/
%dir %_datadir/gstreamer-%majorminor/presets
%_datadir/gstreamer-%majorminor/presets/*

%package -n %bname-soup
Summary:  GStreamer HTTP plugin based on libsoup
Group:    System/Libraries
Requires: %bname-plugins = %{version}
BuildRequires: libsoup-devel >= 2.3

%description -n %bname-soup
Plug-in for HTTP access based on libsoup.

%files -n %bname-soup
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstsouphttpsrc.so

%package -n %bname-pulse
Summary: Pulseaudio plugin for GStreamer
Group: Sound
Requires:      %bname-plugins >= %{version}
BuildRequires: libpulseaudio-devel >= 0.9.7
Requires: pulseaudio >= 0.9.7

%description -n %bname-pulse
This is a GStreamer audio output plugin using the Pulseaudio sound server.

%files -n %bname-pulse
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstpulse.so


### LIBDV ###
%package -n %bname-dv
Summary:       GStreamer DV plug-in
Group:         Video
Requires:      %bname-plugins >= %{version}
BuildRequires: libdv-devel >= 0.98

%description -n %bname-dv
Plug-in for digital video support using libdv.

%files -n %bname-dv
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstdv.so

%package -n %bname-speex
Summary: Gstreamer plugin for encoding and decoding Ogg Speex audio files
Group: Sound
Requires: %bname-plugins >= %{version}-%release
BuildRequires: libspeex-devel 

%description -n %bname-speex
Plug-Ins for creating and playing Ogg Speex audio files.

%files -n %bname-speex  
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstspeex.so

### RAW1394 ###
%package -n %bname-raw1394
Summary:       GStreamer raw1394 Firewire plug-in
Group:         System/Libraries
Requires:      %bname-plugins >= %{version}-%release
BuildRequires: libavc-devel
BuildRequires: libraw1394-devel
BuildRequires: libiec61883-devel

%description -n %bname-raw1394
Plug-in for digital video support using raw1394.

%files -n %bname-raw1394
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgst1394.so

### FLAC ###
%package -n %bname-flac
Summary:       GStreamer plug-in for FLAC lossless audio
Group:         Sound
Requires:      %bname-plugins >= %{version}-%release
BuildRequires: libflac-devel >= 1.0.4

%description -n %bname-flac
Plug-in for the free FLAC lossless audio format.

%files -n %bname-flac
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstflac.so

### ESD ###
%package -n %bname-esound
Summary: Gstreamer plugin for ESD sound output
Group: Sound
Obsoletes:     %bname-esd
Provides:      %bname-esd
Requires: esound >= 0.2.8
BuildRequires: libesound-devel >= 0.2.8
Requires: %bname-plugins >= %{version}-%release
Provides:	%bname-audiosrc
Provides:	%bname-audiosink

%description -n %bname-esound
Output plugin for GStreamer for use with the esound package

%files -n %bname-esound
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstesd.so

### AALIB ###
%package -n %bname-aalib
Summary: Gstreamer plugin for Ascii-art output
Group: Video
BuildRequires: aalib-devel >= 1.3
Requires: %bname-plugins >= %{version}-%release

%description -n %bname-aalib
Plugin for viewing movies in Ascii-art using aalib library.

%files -n %bname-aalib
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstaasink.so

%package -n %bname-caca
Summary: Gstreamer plugin for Ascii-art output
Group: Video
BuildRequires: libcaca-devel
Requires: %bname-plugins >= %{version}-%release

%description -n %bname-caca
Plugin for viewing movies in Ascii-art using caca library.

%files -n %bname-caca
%defattr(-, root, root)
%_libdir/gstreamer-%majorminor/libgstcacasink.so


%package -n %bname-wavpack
Summary: Gstreamer plugin for encoding and decoding WavPack audio files
Group: Sound
Requires: %bname-plugins = %{version}
BuildRequires: libwavpack-devel

%description -n %bname-wavpack
Plug-Ins for creating and playing WavPack audio files.

%files -n %bname-wavpack
%defattr(-, root, root)
%{_libdir}/gstreamer-%{majorminor}/libgstwavpack.so


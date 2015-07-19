%define oname	gst-plugins-good
%define api	0.10
%define bname	gstreamer%{api}
%bcond_with esd

Summary:	GStreamer Streaming-media framework plug-ins
Name:		%{bname}-plugins-good
Version:	0.10.31
Release:	15
License:	LGPLv2+
Group:		Sound
URL:		http://gstreamer.freedesktop.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gst-plugins-good/%{api}/%{oname}-%{version}.tar.xz
# See https://bugzilla.gnome.org/show_bug.cgi?id=681491
Patch0:		gst-plugins-good-0.10.31-linux3.6.patch
# See https://bugs.gentoo.org/show_bug.cgi?id=468618
Patch1:		gst-plugins-v4l2-0.10.31-linux-headers-3.9.patch

BuildRequires:	GConf2
BuildRequires:	gstreamer%{api}-plugins-base
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api})
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(orc-0.4)
BuildRequires:	pkgconfig(shout)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)
%ifarch %{ix86}
BuildRequires:	nasm => 0.90
BuildRequires:	valgrind
%endif

Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink
# gw this is the default http source:
Suggests:	%{bname}-soup
# some plugins moved from bad to good with release 0.10.23
Conflicts:	gstreamer0.10-plugins-bad < 0.10.19

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

%package -n %{bname}-jack
Summary:	GStreamer plug-in for the Jack Sound Server
Group:		Sound
BuildRequires:	pkgconfig(jack)
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink

%description -n %{bname}-jack
Plug-in for the JACK professional sound server.

%files -n %{bname}-jack
%{_libdir}/gstreamer-%{api}/libgstjack.so

%package -n %{bname}-soup
Summary:	GStreamer HTTP plugin based on libsoup
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libsoup-2.4)

%description -n %{bname}-soup
Plug-in for HTTP access based on libsoup.

%files -n %{bname}-soup
%{_libdir}/gstreamer-%{api}/libgstsouphttpsrc.so

%package -n %{bname}-pulse
Summary:	Pulseaudio plugin for GStreamer
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libpulse)

%description -n %{bname}-pulse
This is a GStreamer audio output plugin using the Pulseaudio sound server.

%files -n %{bname}-pulse
%{_libdir}/gstreamer-%{api}/libgstpulse.so

### LIBDV ###
%package -n %{bname}-dv
Summary:	GStreamer DV plug-in
Group:		Video
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libdv)

%description -n %{bname}-dv
Plug-in for digital video support using libdv.

%files -n %{bname}-dv
%{_libdir}/gstreamer-%{api}/libgstdv.so

%package -n %{bname}-speex
Summary:	Gstreamer plugin for encoding and decoding Ogg Speex audio files
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(speex)

%description -n %{bname}-speex
Plug-Ins for creating and playing Ogg Speex audio files.

%files -n %{bname}-speex
%{_libdir}/gstreamer-%{api}/libgstspeex.so

### RAW1394 ###
%package -n %{bname}-raw1394
Summary:	GStreamer raw1394 Firewire plug-in
Group:		System/Libraries
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libiec61883)

%description -n %{bname}-raw1394
Plug-in for digital video support using raw1394.

%files -n %{bname}-raw1394
%{_libdir}/gstreamer-%{api}/libgst1394.so

### FLAC ###
%package -n %{bname}-flac
Summary:	GStreamer plug-in for FLAC lossless audio
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(flac)

%description -n %{bname}-flac
Plug-in for the free FLAC lossless audio format.

%files -n %{bname}-flac
%{_libdir}/gstreamer-%{api}/libgstflac.so

%if %{with esd}
### ESD ###
%package -n %{bname}-esound
Summary:	Gstreamer plugin for ESD sound output
Group:		Sound
Obsoletes:	%{bname}-esd < %{version}-%{release}
Provides:	%{bname}-esd = %{version}-%{release}
Requires:	esound >= 0.2.8
BuildRequires:	pkgconfig(esound)
Requires:	%{bname}-plugins
Provides:	%{bname}-audiosrc
Provides:	%{bname}-audiosink

%description -n %{bname}-esound
Output plugin for GStreamer for use with the esound package

%files -n %{bname}-esound
%{_libdir}/gstreamer-%{api}/libgstesd.so
%endif

### AALIB ###
%package -n %{bname}-aalib
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
BuildRequires:	aalib-devel >= 1.3
Requires:	%{bname}-plugins

%description -n %{bname}-aalib
Plugin for viewing movies in Ascii-art using aalib library.

%files -n %{bname}-aalib
%{_libdir}/gstreamer-%{api}/libgstaasink.so

%package -n %{bname}-caca
Summary:	Gstreamer plugin for Ascii-art output
Group:		Video
BuildRequires:	pkgconfig(caca)
Requires:	%{bname}-plugins

%description -n %{bname}-caca
Plugin for viewing movies in Ascii-art using caca library.

%files -n %{bname}-caca
%{_libdir}/gstreamer-%{api}/libgstcacasink.so

%package -n %{bname}-wavpack
Summary:	Gstreamer plugin for encoding and decoding WavPack audio files
Group:		Sound
Requires:	%{bname}-plugins
BuildRequires:	pkgconfig(wavpack)

%description -n %{bname}-wavpack
Plug-Ins for creating and playing WavPack audio files.

%files -n %{bname}-wavpack
%{_libdir}/gstreamer-%{api}/libgstwavpack.so

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
export CC=gcc
export CXX=g++
%configure  \
	--with-package-name='%{distribution} %{name} package' \
	--with-package-origin='%{disturl}' \
	--disable-dependency-tracking \
	--enable-experimental \
	--disable-hal
%make

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std GETTEXT_PACKAGE=%{oname}-%{api}
%find_lang %{oname}-%{api}

%define schemas gstreamer-0.10

%files -f %{oname}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_sysconfdir}/gconf/schemas/gstreamer-%{api}.schemas
%{_libdir}/gstreamer-%{api}/libgstalaw.so
%{_libdir}/gstreamer-%{api}/libgstannodex.so
%{_libdir}/gstreamer-%{api}/libgstalpha.so
%{_libdir}/gstreamer-%{api}/libgstalphacolor.so
%{_libdir}/gstreamer-%{api}/libgstapetag.so
%{_libdir}/gstreamer-%{api}/libgstaudiofx.so
%{_libdir}/gstreamer-%{api}/libgstaudioparsers.so
%{_libdir}/gstreamer-%{api}/libgstauparse.so
%{_libdir}/gstreamer-%{api}/libgstautodetect.so
%{_libdir}/gstreamer-%{api}/libgstavi.so
%{_libdir}/gstreamer-%{api}/libgstcairo.so
%{_libdir}/gstreamer-%{api}/libgstcutter.so
%{_libdir}/gstreamer-%{api}/libgstdebug.so
%{_libdir}/gstreamer-%{api}/libgstdeinterlace.so
%{_libdir}/gstreamer-%{api}/libgstefence.so
%{_libdir}/gstreamer-%{api}/libgsteffectv.so
%{_libdir}/gstreamer-%{api}/libgstflv.so
%{_libdir}/gstreamer-%{api}/libgstequalizer.so
%{_libdir}/gstreamer-%{api}/libgstflxdec.so
%{_libdir}/gstreamer-%{api}/libgstgconfelements.so
%{_libdir}/gstreamer-%{api}/libgstgdkpixbuf.so
%{_libdir}/gstreamer-%{api}/libgstgoom.so
%{_libdir}/gstreamer-%{api}/libgstgoom2k1.so
%{_libdir}/gstreamer-%{api}/libgsticydemux.so
%{_libdir}/gstreamer-%{api}/libgstid3demux.so
%{_libdir}/gstreamer-%{api}/libgstimagefreeze.so
%{_libdir}/gstreamer-%{api}/libgstinterleave.so
%{_libdir}/gstreamer-%{api}/libgstisomp4.so
%{_libdir}/gstreamer-%{api}/libgstjpeg.so
%{_libdir}/gstreamer-%{api}/libgstlevel.so
%{_libdir}/gstreamer-%{api}/libgstmatroska.so
%{_libdir}/gstreamer-%{api}/libgstmonoscope.so
%{_libdir}/gstreamer-%{api}/libgstmulaw.so
%{_libdir}/gstreamer-%{api}/libgstmultifile.so
%{_libdir}/gstreamer-%{api}/libgstmultipart.so
%{_libdir}/gstreamer-%{api}/libgstnavigationtest.so
%{_libdir}/gstreamer-%{api}/libgstossaudio.so
%{_libdir}/gstreamer-%{api}/libgstoss4audio.so
%{_libdir}/gstreamer-%{api}/libgstpng.so
%{_libdir}/gstreamer-%{api}/libgstreplaygain.so
%{_libdir}/gstreamer-%{api}/libgstrtp.so
%{_libdir}/gstreamer-%{api}/libgstrtpmanager.so
%{_libdir}/gstreamer-%{api}/libgstrtsp.so
%{_libdir}/gstreamer-%{api}/libgstshapewipe.so
%{_libdir}/gstreamer-%{api}/libgstshout2.so
%{_libdir}/gstreamer-%{api}/libgstsmpte.so
%{_libdir}/gstreamer-%{api}/libgstspectrum.so
%{_libdir}/gstreamer-%{api}/libgsttaglib.so
%{_libdir}/gstreamer-%{api}/libgstudp.so
%{_libdir}/gstreamer-%{api}/libgstvideo4linux2.so
%{_libdir}/gstreamer-%{api}/libgstvideobox.so
%{_libdir}/gstreamer-%{api}/libgstvideocrop.so
%{_libdir}/gstreamer-%{api}/libgstvideofilter.so
%{_libdir}/gstreamer-%{api}/libgstvideomixer.so
%{_libdir}/gstreamer-%{api}/libgstwavenc.so
%{_libdir}/gstreamer-%{api}/libgstwavparse.so
%{_libdir}/gstreamer-%{api}/libgstximagesrc.so
%{_libdir}/gstreamer-%{api}/libgsty4menc.so
%dir %{_datadir}/gstreamer-%{api}/
%dir %{_datadir}/gstreamer-%{api}/presets
%{_datadir}/gstreamer-%{api}/presets/*

